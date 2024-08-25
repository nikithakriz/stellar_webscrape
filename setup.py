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
    long_description=open('README.md').read(),  # Make sure README.md is present
    long_description_content_type='text/markdown',
    author='Nikitha Krishnan',
    author_email='nikithakrishnan123@gmail.com',  # Fixed email typo
    url='https://github.com/nikithakrishnan/stellar-webscrape',  # Provide the GitHub repo URL or a relevant URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Add the license you are using
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
