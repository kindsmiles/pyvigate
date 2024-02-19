# Module `scraping`

## Class `Scraping`

### Attributes:


### Methods:

- **__init__**`(self, data_dir='data')`

No description provided.

- **_setup_directories**`(self)`

    Sets up necessary directories for caching.

- **extract_data_from_page**`(self, page)`

    Extracts specific data from the current page using BeautifulSoup.

- **scrape_and_extract_links**`(self, page, base_url)`

    Extracts all unique links that match the base URL domain.

- **scrape_page_content**`(self, page)`

    Scrapes the current page content.

