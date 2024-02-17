import asyncio
import json
from bs4 import BeautifulSoup
from playwright.async_api import Page
import ast
import hashlib
import os
import shutil


class Login:
    def __init__(self, query_engine=None,
                 credentials_file="demo_credentials.json",
                 cache_dir="html_cache"):

        self.query_engine = query_engine
        self.credentials_file = credentials_file
        self.cache_dir = cache_dir
        self._setup_directories()

    def _setup_directories(self):
        """Sets up necessary directories for caching."""
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)
        os.makedirs(self.cache_dir)

    async def is_page_stable(self, page: Page, interval=0.1, checks=4):
        """Check if the page content is stable over a few intervals."""
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
        """Performs login using detected selectors from LlamaIndexWrapper."""
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
        """Caches the current page content for AI analysis."""
        cache_filename = f"{self.cache_dir}/{self.get_filename_from_url(current_url)}_cached.html"
        self.cache_filename = cache_filename
        with open(cache_filename, "w") as file:
            file.write(str(soup))
        return cache_filename

    async def get_selectors_from_ai(self, cache_filename):
        """Uses the LlamaIndexWrapper to analyze cached page content
        and extract login selectors."""
        cache_filename = self.cache_filename
        directory_path = os.path.dirname(cache_filename)
        index = self.query_engine.create_vector_store_index(directory_path)
        query_text = """Look at the given html and find the selectors
                                      corresponding the following fields.
                                      The selectors are required to pass
                                  to the page variable of playwright so respond in
                                  that format.
                                      1) Email Textarea
                                      2) Password Textarea
                                      3) Log In/ Sign In button
                                    Respond only with a dict where the keys are the above three.
                                      """
        response = self.query_engine.query(index, query_text)
        login_selectors = ast.literal_eval(str(response))
        return login_selectors

    def save_login_state(self, url, username, password, actual_url):
        """Saves login state to a file."""
        credentials = {
            "url": url,
            "username": username,
            "password": password,
            "actual_base_url": actual_url
        }
        with open(self.credentials_file, "w") as file:
            json.dump(credentials, file)

    def get_filename_from_url(self, url):
        """Generates a sanitized filename from a URL."""
        # Implementation remains similar to the provided utility function
        pass
