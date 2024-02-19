# Module `engine`

## Class `PlaywrightEngine`

### Attributes:


### Methods:

- **__init__**`(self, headless=True)`

No description provided.

- **click_selector**`(self, selector)`

    Clicks an element specified by a selector.

- **fill_form**`(self, selector, value)`

    Fills form element specified by a selector with the given value.

- **generate_pdf**`(self, path='output.pdf')`

    Generates a PDF of the current page (Chromium only).

- **get_page_content**`(self)`

    Returns the current page's HTML content.

- **navigate_to**`(self, url)`

    Navigates to a given URL.

- **start_browser**`(self)`

    Starts a headless browser session.

- **stop_browser**`(self)`

    Closes the browser session.

- **take_screenshot**`(self, path='screenshot.png')`

    Takes a screenshot of the current page.

- **wait_for_navigation**`(self, timeout=30000)`

    Waits for the page to fully load.

- **wait_for_selector**`(self, selector, timeout=30000)`

    Waits for an element specified by a selector to be present.

