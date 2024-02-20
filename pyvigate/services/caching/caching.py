import os
from urllib.parse import urljoin, urlparse
import shutil

from bs4 import BeautifulSoup
from playwright.async_api import Page


class Caching:
    """
    Manages caching of webpage content for offline access and analysis.

    Attributes:
        cache_dir (str): Directory to store cached pages.
    """

    def __init__(self, cache_dir="html_cache"):
        """
        Initializes the caching system with a specified directory.

        Args:
            cache_dir (str): The directory for storing cache files.
        """
        self.cache_dir = cache_dir
        self._setup_directories()

    def _setup_directories(self):
        """Sets up necessary directories for caching."""
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)
        os.makedirs(self.cache_dir)

    async def cache_page_content(self, page: Page, url: str):
        """
        Saves the HTML content of a page to the cache directory.

        Args:
            page (Page): The page object from Playwright.
            url (str): The URL of the page to cache.

        Returns:
            str: The file path of the cached content.
        """
        await page.goto(url)
        content = await page.content()
        filename = self._get_filename_from_url(url) + "_cached.html"
        cache_filepath = os.path.join(self.cache_dir, filename)

        with open(cache_filepath, "w", encoding="utf-8") as file:
            file.write(content)
        return cache_filepath

    def _get_filename_from_url(self, url: str) -> str:
        """Generates a filename from a URL."""
        parsed_url = urlparse(url)
        filename = parsed_url.netloc.replace("www.",
                                             "") + parsed_url.path.replace(
                                                 '/', '_')
        return filename.strip('_')

    async def cache_all_links(self, page: Page, base_url: str):
        """
        Caches content from all unique links on a given page.

        Args:
            page (Page): The page object from Playwright.
            base_url (str): The base URL to match links against.

        Returns:
            None
        """
        await page.goto(base_url)
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        links = soup.find_all("a", href=True)
        unique_links = set([urljoin(base_url,
                                    link.get(
                                        "href")) for link in links if link.get(
                                            "href")])

        for link in unique_links:
            if urlparse(link).netloc == urlparse(base_url).netloc:
                await self.cache_page_content(page, link)
