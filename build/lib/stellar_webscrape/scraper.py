import time
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .utils import initialize_driver, save_to_file, load_urls_from_file
from .config import Config

logger = logging.getLogger(__name__)

def scrape_content(driver, url):
    """
    Scrapes text content from the given URL using the provided WebDriver.
    
    Args:
        driver (webdriver.Chrome): The initialized WebDriver instance.
        url (str): The URL to scrape content from.
    
    Returns:
        str: The scraped content from the page, or None if an error occurs.
    """
    try:
        driver.get(url)
        logger.info(f"Loading page: {url}")
        time.sleep(Config['delay'])
        try:
            content = driver.find_element(By.TAG_NAME, 'body').text
            logger.info(f"Content scraped from {url}: {content[:100]}...")  # Log the first 100 characters for debugging
            return content
        except NoSuchElementException:
            logger.error(f"Element with tag name 'body' not found on {url}")
            return None
    except TimeoutException as e:
        logger.error(f"Timeout while scraping {url}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error while scraping {url}: {e}")
        return None

def main(urls=None, file_path=None, save_folder=None):
    """
    Main function to handle the web scrapping process.
    
    Args:
        urls (list, optional): A list of URLs to scrape. If not provided, `file_path` must be given.
        save_folder (str, optional): Directory path to save the scraped content. 
            If not provided, files will be saved in the current directory[which will be messy ofcourse! it will be better to provide save_folder :) ].

    Raises:
        ValueError: If both `urls` and `file_path` are not provided.
        
    """
    
    if urls is None and file_path is None:
        raise ValueError("Either 'urls' or 'file_path' must be provided.")
    
    if file_path:
        urls = load_urls_from_file(file_path)

    if not urls:
        logger.error("No URLs to scrape. Exiting.")
        return
    
    driver = initialize_driver()
    
    try:
        for url in urls:
            logger.info(f"Scraping {url}...")
            content = scrape_content(driver, url)
            if content:
                save_to_file(url, content, save_folder)
            time.sleep(Config['request_delay'])
    finally:
        driver.quit()
        logger.info("WebDriver closed.")
