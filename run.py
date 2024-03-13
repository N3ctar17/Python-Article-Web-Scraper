# This is the main program that imports and utilizes functionalities from other modules.

from module_2.some_name2 import scrape_and_save

if __name__ == "__main__":
    url_file = "urls.txt"  # Path to the file containing URLs
    scrape_and_save(url_file)
