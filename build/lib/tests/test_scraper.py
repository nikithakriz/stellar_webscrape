import pytest
from stellar_webscrape.scraper import scrape_content
from stellar_webscrape.utils import initialize_driver

WIKI_URLS = [
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/wiki/Web_scraping'
]

@pytest.fixture(scope="module")
def driver():
    """Initialize WebDriver for testing."""
    driver = initialize_driver(headless=True)
    yield driver
    driver.quit()

def test_scrape_content(driver):
    """
    Test the scrape_content function for different Wikipedia URLs using a real WebDriver.
    """
    for url in WIKI_URLS:
        content = scrape_content(driver, url)
        assert content is not None
        assert isinstance(content, str)
        
        if "Python_(programming_language)" in url:

            # assert "interpreted high-level general-purpose programming language" in content
            assert "Guido van Rossum" in content  # Example of another expected phrase
            
        elif "Web_scraping" in url:
            assert "web scraping" in content
            assert "data extraction" in content  # Example of another expected phrase
