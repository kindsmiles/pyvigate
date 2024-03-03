from playwright.async_api import async_playwright


class PlaywrightEngine:
    """
    Manages browser automation tasks using Playwright in a headless or GUI mode.

    Attributes:
        headless (bool): Whether to run the browser in headless mode.
        browser: Instance of the browser being used.
        page: Current page object from the browser.
    """

    def __init__(self, headless=True):
        """
        Initializes the Playwright engine with optional headless mode.

        Args:
            headless (bool, optional): Run browser in headless mode. Defaults to True.
        """
        self.headless = headless
        self.browser = None
        self.page = None

    async def start_browser(self):
        """
        Starts a Playwright browser session based on the headless preference.
        """
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(headless=self.headless)
        self.page = await self.browser.new_page()

    async def stop_browser(self):
        """
        Closes the current browser session and all associated pages.
        """
        await self.browser.close()

    async def navigate_to(self, url):
        """
        Navigates the current page to a specified URL.

        Args:
            url (str): The URL to navigate to.

        Returns:
            The current page object after navigation.
        """
        if not self.page:
            raise Exception("Browser isn't started. Call start_browser first.")
        await self.page.goto(url)
        return self.page

    async def click_selector(self, selector):
        """
        Clicks on an element on the page identified by the given selector.

        Args:
            selector (str): The selector of the element to click.
        """
        await self.page.click(selector)

    async def fill_form(self, selector, value):
        """
        Fills a form element identified by the given selector with a value.

        Args:
            selector (str): The selector of the form element.
            value (str): The value to fill in the form element.
        """
        await self.page.fill(selector, value)

    async def wait_for_navigation(self, timeout=30000):
        """
        Waits for the page to navigate and fully load.

        Args:
            timeout (int, optional): Maximum time to wait for navigation. Defaults to 30000 ms.
        """
        await self.page.wait_for_load_state("networkidle", timeout=timeout)

    async def wait_for_selector(self, selector, timeout=30000):
        """
        Waits for an element to be present on the page, specified by a selector.

        Args:
            selector (str): The selector of the element to wait for.
            timeout (int, optional): Maximum time to wait for the element. Defaults to 30000 ms.
        """
        await self.page.wait_for_selector(selector, state="attached", timeout=timeout)

    async def take_screenshot(self, path="screenshot.png"):
        """
        Takes a screenshot of the current page.

        Args:
            path (str, optional): The file path where the screenshot will be saved. Defaults to "screenshot.png".
        """
        await self.page.screenshot(path=path)

    async def generate_pdf(self, path="output.pdf"):
        """
        Generates a PDF of the current page. Only available in Chromium.

        Args:
            path (str, optional): The file path where the PDF will be saved. Defaults to "output.pdf".
        """
        await self.page.pdf(path=path)

    async def execute_actions(self, action_sequence: list):
        """
        Executes a sequence of actions based on the action method strings.
    
        Args:
            action_sequence (list): A list of dictionaries where each dictionary
            represents an action and its corresponding arguments.
        """
        action_methods = {
            'navigate_to': self.navigate_to,
            'click_selector': self.click_selector,
            'take_screenshot': self.take_screenshot,
            'wait_for_selector': self.wait_for_selector,
            'wait_for_navigation': self.wait_for_navigation,
            'generate_pdf': self.generate_pdf,
            'fill_form': self.fill_form
            # Add other action mappings as needed.
        }
    
        for action in action_sequence:
            action_name = action.get("action")
            args = action.get("args", [])
            kwargs = action.get("kwargs", {})
    
            if action_name in action_methods:
                method = action_methods[action_name]
                await method(*args, **kwargs)
            else:
                print(f"No method found for action: {action_name}")
