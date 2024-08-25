# StellarWebScrape

StellarWebScrape is a Python package for web scraping using Selenium. It allows you to scrape text content from web pages and save it to files.

## Installation

To install StellarWebScrape, You can install the package from `TestPyPI`:

```sh
pip install stellar-webscrape==0.1.1
```

or you clone the repository and use `pip`:

```bash
pip install .

```

## Usage
You can run the scraper from the command line or use it programmatically:

### Command Line
To scrape content from URLs listed in a JSON file and save them to a specified folder:

```bash
stellar-webscrape --file_path=data.json --save_folder=saved_content
```

### Programmatic Usage
You can also use the package programmatically in your Python code:
```python
from stellar_webscrape.scraper import main

urls = ["https://example.com", "https://another-example.com"]
main(urls=urls, save_folder="scraped_data")

```
## ⚙️  Configuration
Configuration options can be adjusted in *stellar_webscrape/config*.py. By default, `scraping delays` are set to 3 seconds, and `request delays` are set to 5 seconds.

## Testing
To run tests, use pytest:
```bash
pytest
```

## 📜 License
This project is licensed under the MIT License.
