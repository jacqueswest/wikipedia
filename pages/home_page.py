from selenium.webdriver.common.by import By
from wikipedia.pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://en.wikipedia.org/")

    def search(self, term):
        # Use the method from BasePage to wait for elements to be clickable
        search_input = self.wait_for_element(*self.SEARCH_INPUT)
        search_input.send_keys(term)

        search_button = self.wait_for_element(*self.SEARCH_BUTTON)
        search_button.click()
