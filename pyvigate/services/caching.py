import os
from urllib.parse import urljoin, urlparse
import shutil

from bs4 import BeautifulSoup
from playwright.async_api import Page


class Caching:
    def __init__(self, cache_dir="html_cache"):
        self.cache_dir = cache_dir
        self._setup_directories()

    def _setup_directories(self):
        """Sets up necessary directories for caching."""
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)
        os.makedirs(self.cache_dir)

    async def cache_page_content(self, page: Page, url: str):
        """Caches the HTML content of a given URL."""
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
        """Caches all unique links found on the given page."""
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
