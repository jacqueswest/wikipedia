from wikipedia.pages.home_page import HomePage
from wikipedia.pages.search_results_page import SearchResultsPage


def test_search_wikipedia(driver):
    home_page = HomePage(driver)
    home_page.search("Automation testing")

    search_results_page = SearchResultsPage(driver)

    # Verify page title
    assert search_results_page.get_tab_title() == "Test automation - Wikipedia"

    # Verify article title
    assert search_results_page.verify_article_title("Test automation")

    # Verify content contains specific text
    expected_text = "Test automation can automate some repetitive but necessary tasks in a formalized testing process"
    assert search_results_page.verify_content_contains_text(expected_text)
