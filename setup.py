from setuptools import setup, find_packages

setup(
    name='stellar_webscrape',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver-manager',
    ],
    entry_points={
        'console_scripts': [
            'stellar-webscrape = stellar_webscrape.scraper:main',
        ],
    },
    description='A Python package for web scraping with Selenium.',
    author='Nikitha Krishnan',
    author_email='nikithakrishnan123@gmailcom',
    url='',
)
