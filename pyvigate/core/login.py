import asyncio
import json
from bs4 import BeautifulSoup
from playwright.async_api import Page
import ast
import hashlib
import os
import shutil


class Login:
    """
    Automates web application login using AI-powered selector detection.

    Attributes:
        llm_agent: An instance of QueryEngine used for selector detection.
        credentials_file (str): Path to a JSON file storing login credentials.
        cache_dir (str): Directory path for caching webpage contents.
    """

    def __init__(self, llm_agent=None,
                 credentials_file="demo_credentials.json",
                 cache_dir="html_cache"):

        self.llm_agent = llm_agent
        self.credentials_file = credentials_file
        self.cache_dir = cache_dir
        self._setup_directories()

    def _setup_directories(self):
        """Sets up necessary directories for caching."""
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)
        os.makedirs(self.cache_dir)

    async def is_page_stable(self, page: Page, interval=0.1, checks=4):
        """
        Verifies if the webpage content is stable over a series of intervals.

        Args:
            page (Page): The Playwright page instance to check.
            interval (float): The delay between checks.
            checks (int): The number of checks to determine stability.

        Returns:
            bool: True if stable, False otherwise.
        """
        last_html_hash = ""
        stable_checks = 0
        while stable_checks < checks:
            await asyncio.sleep(interval)
            current_html = await page.content()
            current_hash = hashlib.md5(current_html.encode()).hexdigest()
            if current_hash == last_html_hash:
                stable_checks += 1
            else:
                stable_checks = 0
            last_html_hash = current_hash
        return stable_checks >= checks

    async def perform_login(self,
                            page: Page, url: str,
                            username: str,
                            password: str):
        """
        Performs the login action on the specified webpage.

        Args:
            page (Page): The Playwright page instance
            url (str): The URL of the login page.
            username (str): The username for login.
            password (str): The password for login.

        Returns:
            Page: The page instance after the login action.
        """
        await page.goto(url)
        await self.is_page_stable(page)
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")

        # Cache the page content for AI analysis
        cache_filename = self.cache_page_content(soup, page.url)

        # Use the AI to get selectors
        login_selectors = await self.get_selectors_from_ai(cache_filename)

        # Perform login actions
        await page.fill(login_selectors["Email Textarea"], username)
        await page.fill(login_selectors["Password Textarea"], password)
        await page.click(login_selectors["Log In/ Sign In button"])
        await page.wait_for_load_state("load")

        # Optionally, save the actual URL after login
        self.save_login_state(url, username, password, page.url)
        return page

    def cache_page_content(self, soup, current_url):
        """
        Caches the HTML content of the current page for AI analysis.

        Args:
            soup (BeautifulSoup): BeautifulSoup instance
            current_url (str): The current page URL.

        Returns:
            str: The filepath of the cached content.
        """
        cache_filename = f"{self.cache_dir}/{self._get_filename_from_url(current_url)}_cached.html"
        self.cache_filename = cache_filename
        with open(cache_filename, "w") as file:
            file.write(str(soup))
        return cache_filename

    async def get_selectors_from_ai(self, cache_filename):
        """
        Uses AI to analyze cached page content and extract login selectors.

        Args:
            cache_filename (str): The filepath of the cached page content.

        Returns:
            dict: A dictionary of detected login selectors.
        """

        query_text = """Look at the given html and find the selectors
                                      corresponding the following fields.
                                      The selectors are required to pass
                                  to the page variable of playwright.
                                  Respond only with a python dict in 
                                  the following format:
                                      {'Email Textarea': 'value',
                                      'Password Textarea': value',
                                      'Log In/ Sign In button': value'
                                      }
                                      """
        response = self.llm_agent.query(query_text)
        login_selectors = ast.literal_eval(str(response))
        return login_selectors

    def save_login_state(self, url, username, password, actual_url):
        """
        Saves the current login state to a credentials file.

        Args:
            url (str): The login page URL.
            username (str): The username used for login.
            password (str): The password used for login.
            actual_url (str): The URL after successful login.
        """
        credentials = {
            "url": url,
            "username": username,
            "password": password,
            "actual_base_url": actual_url
        }
        with open(self.credentials_file, "w") as file:
            json.dump(credentials, file)

    def _get_filename_from_url(self, url):

        filename = url.replace("http://",
                               "").replace("https://", "").replace("/", "_")
        return filename.strip("_")
