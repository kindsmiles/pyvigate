# Module `login`

## Class `Login`

    Automates web application login using AI-powered selector detection.
    
    Attributes:
        query_engine: An instance of QueryEngine used for selector detection.
        credentials_file (str): Path to a JSON file storing login credentials.
        cache_dir (str): Directory path for caching webpage contents.

### Attributes:


### Methods:

- **__init__**`(self, query_engine=None, credentials_file='demo_credentials.json', cache_dir='html_cache')`

No description provided.

- **_get_filename_from_url**`(self, url)`

No description provided.

- **_setup_directories**`(self)`

    Sets up necessary directories for caching.

- **cache_page_content**`(self, soup, current_url)`

    Caches the HTML content of the current page for AI analysis.
    
    Args:
        soup (BeautifulSoup): BeautifulSoup instance
        current_url (str): The current page URL.
    
    Returns:
        str: The filepath of the cached content.

- **get_selectors_from_ai**`(self, cache_filename)`

    Uses AI to analyze cached page content and extract login selectors.
    
    Args:
        cache_filename (str): The filepath of the cached page content.
    
    Returns:
        dict: A dictionary of detected login selectors.

- **is_page_stable**`(self, page: playwright.async_api._generated.Page, interval=0.1, checks=4)`

    Verifies if the webpage content is stable over a series of intervals.
    
    Args:
        page (Page): The Playwright page instance to check.
        interval (float): The delay between checks.
        checks (int): The number of checks to determine stability.
    
    Returns:
        bool: True if stable, False otherwise.

- **perform_login**`(self, page: playwright.async_api._generated.Page, url: str, username: str, password: str)`

    Performs the login action on the specified webpage.
    
    Args:
        page (Page): The Playwright page instance
        url (str): The URL of the login page.
        username (str): The username for login.
        password (str): The password for login.
    
    Returns:
        Page: The page instance after the login action.

- **save_login_state**`(self, url, username, password, actual_url)`

    Saves the current login state to a credentials file.
    
    Args:
        url (str): The login page URL.
        username (str): The username used for login.
        password (str): The password used for login.
        actual_url (str): The URL after successful login.

