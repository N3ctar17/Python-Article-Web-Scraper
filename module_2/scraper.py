# SOLID Principle: Single Responsibility
# This module is responsible for extracting domain and scraping data from URLs.

import os
from urllib.parse import urlparse
from module_1.format import get_text_from_url

def extract_domain(url):
    """
    Extract the domain name from a given URL.

    Args:
    - url (str): The URL to extract the domain from.

    Returns:
    - str: The domain name.
    """
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    return domain

def scrape_and_save(url_file):
    """
    Scrape text content from URLs listed in a file and save them.

    Args:
    - url_file (str): Path to the file containing URLs.
    """
    url_file = "data/raw/urls.txt"  # Path to the file containing URLs
    with open(url_file, 'r') as f:
        for i, url in enumerate(f):
            url = url.strip()
            if url:
                if not url.startswith("http://") and not url.startswith("https://"):
                    url = "https://" + url
                text = get_text_from_url(url)
                if text:
                    domain = extract_domain(url)
                    if not os.path.exists("data/raw"):
                        os.makedirs("data/raw")
                    if not os.path.exists("data/processed"):
                        os.makedirs("data/processed")
                    with open(os.path.join("data/processed", f"scraped_text_{i+1}.txt"), 'w', encoding='utf-8') as text_file:
                        text_file.write(text)

