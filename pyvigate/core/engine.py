from playwright.async_api import async_playwright


class PlaywrightEngine:
    def __init__(self, headless=True):
        self.headless = headless
        self.browser = None
        self.page = None

    async def start_browser(self):
        """Starts a headless browser session."""
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(headless=self.headless)
        self.page = await self.browser.new_page()

    async def stop_browser(self):
        """Closes the browser session."""
        await self.browser.close()

    async def navigate_to(self, url):
        """Navigates to a given URL."""
        if not self.page:
            raise Exception("Browser isn't started. Call start_browser first.")
        await self.page.goto(url)
        return self.page

    async def get_page_content(self):
        """Returns the current page's HTML content."""
        if not self.page:
            raise Exception("Browser isn't started. Call start_browser first.")
        return await self.page.content()

    async def click_selector(self, selector):
        """Clicks an element specified by a selector."""
        await self.page.click(selector)

    async def fill_form(self, selector, value):
        """Fills form element specified by a selector with the given value."""
        await self.page.fill(selector, value)

    async def wait_for_navigation(self, timeout=30000):
        """Waits for the page to fully load."""
        await self.page.wait_for_load_state("networkidle", timeout=timeout)

    async def wait_for_selector(self, selector, timeout=30000):
        """Waits for an element specified by a selector to be present."""
        await self.page.wait_for_selector(selector,
                                          state="attached",
                                          timeout=timeout)

    async def take_screenshot(self, path="screenshot.png"):
        """Takes a screenshot of the current page."""
        await self.page.screenshot(path=path)

    async def generate_pdf(self, path="output.pdf"):
        """Generates a PDF of the current page (Chromium only)."""
        await self.page.pdf(path=path)
