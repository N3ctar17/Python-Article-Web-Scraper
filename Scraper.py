import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

def get_text_from_url(url):
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
                # Find the index of "after newsletter promotion"
                after_newsletter_index = text.find("after newsletter promotion")
                if after_newsletter_index != -1:
                    # Remove the content between newsletter_index and after_newsletter_index
                    text = text[:newsletter_index]
            return text.strip()
        else:
            print("Article content not found.")
            return None
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return None




def extract_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    return domain

def scrape_and_save(url_file):
    with open(url_file, 'r') as f:
        for i, url in enumerate(f):
            url = url.strip()
            if url:
                # Ensure the URL is properly formatted
                if not url.startswith("http://") and not url.startswith("https://"):
                    url = "https://" + url
                text = get_text_from_url(url)
                if text:
                    domain = extract_domain(url)
                    # Create a directory for each domain if it doesn't exist
                    if not os.path.exists(domain):
                        os.makedirs(domain)
                    # Write text to a file
                    with open(os.path.join(domain, f"scraped_text_{i+1}.txt"), 'w', encoding='utf-8') as text_file:
                        text_file.write(text)

if __name__ == "__main__":
    url_file = "urls.txt"  # Path to the file containing URLs
    scrape_and_save(url_file)
