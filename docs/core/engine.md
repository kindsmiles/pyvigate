# Module `engine`

## Class `PlaywrightEngine`

    Manages browser automation tasks using Playwright in a headless or GUI mode.
    
    Attributes:
        headless (bool): Whether to run the browser in headless mode.
        browser: Instance of the browser being used.
        page: Current page object from the browser.

### Attributes:


### Methods:

- **__init__**`(self, headless=True)`

    Initializes the Playwright engine with optional headless mode.
    
    Args:
        headless (bool, optional): Run browser in headless mode. Defaults to True.

- **click_selector**`(self, selector)`

    Clicks on an element on the page identified by the given selector.
    
    Args:
        selector (str): The selector of the element to click.

- **fill_form**`(self, selector, value)`

    Fills a form element identified by the given selector with a value.
    
    Args:
        selector (str): The selector of the form element.
        value (str): The value to fill in the form element.

- **generate_pdf**`(self, path='output.pdf')`

    Generates a PDF of the current page. Only available in Chromium.
    
    Args:
        path (str, optional): The file path where the PDF will be saved. Defaults to "output.pdf".

- **get_page_content**`(self)`

    Retrieves the HTML content of the current page.
    
    Returns:
        str: The HTML content of the current page.

- **navigate_to**`(self, url)`

    Navigates the current page to a specified URL.
    
    Args:
        url (str): The URL to navigate to.
    
    Returns:
        The current page object after navigation.

- **start_browser**`(self)`

    Starts a Playwright browser session based on the headless preference.

- **stop_browser**`(self)`

    Closes the current browser session and all associated pages.

- **take_screenshot**`(self, path='screenshot.png')`

    Takes a screenshot of the current page.
    
    Args:
        path (str, optional): The file path where the screenshot will be saved. Defaults to "screenshot.png".

- **wait_for_navigation**`(self, timeout=30000)`

    Waits for the page to navigate and fully load.
    
    Args:
        timeout (int, optional): Maximum time to wait for navigation. Defaults to 30000 ms.

- **wait_for_selector**`(self, selector, timeout=30000)`

    Waits for an element to be present on the page, specified by a selector.
    
    Args:
        selector (str): The selector of the element to wait for.
        timeout (int, optional): Maximum time to wait for the element. Defaults to 30000 ms.

