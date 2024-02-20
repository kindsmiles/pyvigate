# Module `caching`

## Class `Caching`

    Manages caching of webpage content for offline access and analysis.
    
    Attributes:
        cache_dir (str): Directory to store cached pages.

### Attributes:


### Methods:

- **__init__**`(self, cache_dir='html_cache')`

    Initializes the caching system with a specified directory.
    
    Args:
        cache_dir (str): The directory for storing cache files.

- **_get_filename_from_url**`(self, url: str) -> str`

    Generates a filename from a URL.

- **_setup_directories**`(self)`

    Sets up necessary directories for caching.

- **cache_all_links**`(self, page: playwright.async_api._generated.Page, base_url: str)`

    Caches content from all unique links on a given page.
    
    Args:
        page (Page): The page object from Playwright.
        base_url (str): The base URL to match links against.
    
    Returns:
        None

- **cache_page_content**`(self, page: playwright.async_api._generated.Page, url: str)`

    Saves the HTML content of a page to the cache directory.
    
    Args:
        page (Page): The page object from Playwright.
        url (str): The URL of the page to cache.
    
    Returns:
        str: The file path of the cached content.

