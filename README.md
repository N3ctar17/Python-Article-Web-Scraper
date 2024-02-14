# Web Scraper

This is a simple web scraper script written in Python using the BeautifulSoup library to extract text content from web pages. It can be used to scrape articles from various websites and save the extracted text to individual text files.  This is modified to mainly work with articles from theguardian.com, but can be modified to work on different websites as well.

## Requirements

- Python 3.9
- BeautifulSoup library (`pip install beautifulsoup4`)
- requests library (`pip install requests`)

## Usage

1. Create an environment with "conda create -n your_environment_name --file requirements.yml"
2. Activate the environment with "conda activate your_environment_name"
3. Create a file named `urls.txt` in the same directory as the script.
4. Add the URLs of the web pages you want to scrape to `urls.txt`, with each URL on a new line.  If the URL does not contian "https://" it will add it for you.
5. Run the Scraper.py file in the terminal using "python3 Scraper.py". It will read the URLs from `urls.txt`, scrape the text content from each page, and save it to individual text files in folders named after the domain of each URL.
6. If getting extra outputs, or not desired outputs, change the contents of the text.find("") fields to skip past unnecessarry parts.

```python
python scraper.py
