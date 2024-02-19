# Module `caching`

## Class `Caching`

### Attributes:


### Methods:

- **__init__**`(self, cache_dir='html_cache')`

No description provided.

- **_get_filename_from_url**`(self, url: str) -> str`

    Generates a filename from a URL.

- **_setup_directories**`(self)`

    Sets up necessary directories for caching.

- **cache_all_links**`(self, page: playwright.async_api._generated.Page, base_url: str)`

    Caches all unique links found on the given page.

- **cache_page_content**`(self, page: playwright.async_api._generated.Page, url: str)`

    Caches the HTML content of a given URL.

