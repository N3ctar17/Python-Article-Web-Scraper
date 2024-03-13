# SOLID Principle: Single Responsibility
# This module is responsible for extracting text from a URL.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_text_from_url(url):
    """
    Extract text content from a given URL.

    Args:
    - url (str): The URL to extract text from.

    Returns:
    - str: Extracted text content from the URL.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove unnecessary tags and whitespace
        article = soup.find("article")
        if article:
            # Remove leading whitespace
            text = article.get_text(separator='\n').strip()
            # Remove unnecessary tags
            for tag in article.find_all(["nav", "aside", "footer"]):
                tag.extract()
            # Find the index of the "Last modified" line and cut everything before it
            last_modified_index = text.find("Last modified")
            if last_modified_index != -1:
                text = text[last_modified_index:]
            # Find the "Explore more on these topics" line and cut everything below it
            explore_index = text.find("Explore more on these topics")
            if explore_index != -1:
                text = text[:explore_index]
            # Find the index of the newsletter promotion and cut everything after it
            newsletter_index = text.find("skip past newsletter promotion")
            if newsletter_index != -1:
                after_newsletter_index = text.find("after newsletter promotion")
                if after_newsletter_index != -1:
                    text = text[:newsletter_index]
            return text.strip()
        else:
            print("Article content not found.")
            return None
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return None
