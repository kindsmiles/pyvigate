from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import os
import shutil


class Scraping:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self._setup_directories()

    async def scrape_page_content(self, page):
        """Scrapes the current page content."""
        content = await page.content()
        return content

    async def extract_data_from_page(self, page):
        """Extracts specific data from the current page using BeautifulSoup."""
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')

        # Example extraction: Getting all text
        page_text = soup.get_text(separator=' ', strip=True)
        return page_text

    async def scrape_and_extract_links(self, page, base_url):
        """Extracts all unique links that match the base URL domain."""
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
