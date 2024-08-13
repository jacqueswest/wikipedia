from selenium.webdriver.common.by import By
from wikipedia.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    ARTICLE_TITLE = (By.ID, "firstHeading")
    ARTICLE_CONTENT = (By.ID, "bodyContent")

    def get_tab_title(self):
        return self.driver.title

    def verify_article_title(self, expected_title):
        title_element = self.wait_for_element(*self.ARTICLE_TITLE)
        return title_element.text == expected_title

    def verify_content_contains_text(self, text):
        content_element = self.wait_for_element(*self.ARTICLE_CONTENT)
        return text in content_element.text
