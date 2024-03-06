from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import os
import shutil


class Scraping:
    """
    A class for scraping web pages using BeautifulSoup.

    Attributes:
        data_dir (str): The directory where scraped data will be stored.
    """

    def __init__(self, page, data_dir="data"):
        """
        Initializes the Scraping class with a specified data directory.

        Parameters:
            page (Page): A playwright page object.
            data_dir (str): The directory to store scraped data.
            Defaults to "data".
        """
        self.page = page
        self.data_dir = data_dir
        self._setup_directories()

    async def scrape_page_content(self):
        """
        Asynchronously scrapes the content of a web page.

        Returns:
            str: The HTML content of the page.
        """
        content = await self.page.content()
        return content

    async def extract_data_from_page(self, url):
        """
        Asynchronously extracts specific data from
        a web page using BeautifulSoup.

        Returns:
            str: Extracted text from the web page.
        """
        await self.page.goto(url)
        content = await self.page.content()
        soup = BeautifulSoup(content, 'html.parser')

        # Example extraction: Getting all text
        page_text = soup.get_text(separator=' ', strip=True)
        return page_text

    async def scrape_and_extract_links(self, url):
        """
        Asynchronously extracts all unique links
        from a web page that match the base URL's domain.

        Parameters:
            base_url (str): The base URL to match links against.

        Returns:
            set: A set of unique URLs
            found on the page that match the base URL's domain.
        """
        page = self.page
        base_url = url
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a', href=True)
        unique_links = {urljoin(base_url,
                                link['href']) for link in links if urlparse(
                                    link['href']).netloc == urlparse(
                                        base_url).netloc}

        return unique_links

    def _setup_directories(self):
        """Sets up necessary directories for caching."""
        if os.path.exists(self.data_dir):
            shutil.rmtree(self.data_dir)
        os.makedirs(self.data_dir)
