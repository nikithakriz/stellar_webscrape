import os
import json
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


logger = logging.getLogger(__name__)

def initialize_driver(headless=True):
    """
    Initializes the Chrome WebDriver with optional configurations.
    
    Args:
        headless (bool): If True, the WebDriver will run in headless mode (without GUI).
                            Defaults to True.
    
    Returns:
        webdriver.Chrome: A Chrome WebDriver instance.
    """
    options = Options()
    if headless:
        options.add_argument('--headless')  # Run in headless mode (without GUI)
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def save_to_file(url, content, save_folder=None):
    """
    Saves the scraped content to a text file.

    Args:
        url (str): The URL corresponding to the content.
        content (str): The text content to save.
        save_folder (str, optional): The folder path where the file will be saved. If not provided, the file will be saved in the current directory.

    Returns:
        None
    """
    file_name = url.replace('https://', '').replace('/', '_') + ".txt"
    if save_folder:
        os.makedirs(save_folder, exist_ok=True)
        file_path = os.path.join(save_folder, file_name)
    else:
        file_path = file_name
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    
    logger.info(f"Content saved to {file_path}")
    
def load_urls_from_file(file_path):
    """
    Loads a list of URLs from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing URLs.

    Returns:
        list: A list of URLs extracted from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contents cannot be parsed as JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        urls = []
        for value in data.values():
            urls.extend(value.get("urls", []))
        
        return urls
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading URLs from {file_path}: {e}")
        return []
    

