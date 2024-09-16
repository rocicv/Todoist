# core/webdriver.py

from playwright.sync_api import sync_playwright

class WebDriver:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start_browser(self, url):
        if self.playwright is not None:
            raise RuntimeError("Browser already started")
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto(url)

    def close_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
