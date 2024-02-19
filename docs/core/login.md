# Module `login`

## Class `Login`

### Attributes:


### Methods:

- **__init__**`(self, query_engine=None, credentials_file='demo_credentials.json', cache_dir='html_cache')`

No description provided.

- **_setup_directories**`(self)`

    Sets up necessary directories for caching.

- **cache_page_content**`(self, soup, current_url)`

    Caches the current page content for AI analysis.

- **get_filename_from_url**`(self, url)`

    Generates a sanitized filename from a URL.

- **get_selectors_from_ai**`(self, cache_filename)`

    Uses the LlamaIndexWrapper to analyze cached page content
    and extract login selectors.

- **is_page_stable**`(self, page: playwright.async_api._generated.Page, interval=0.1, checks=4)`

    Check if the page content is stable over a few intervals.

- **perform_login**`(self, page: playwright.async_api._generated.Page, url: str, username: str, password: str)`

    Performs login using detected selectors from LlamaIndexWrapper.

- **save_login_state**`(self, url, username, password, actual_url)`

    Saves login state to a file.

