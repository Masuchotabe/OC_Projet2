import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from extract import extract_book_data
from store_data import store_in_csv
from navigate import browse_category
import pprint

pp = pprint.PrettyPrinter(sort_dicts=False)

home_url = "http://books.toscrape.com/index.html"

home_page = requests.get(home_url)
home_soup = BeautifulSoup(home_page.content, 'html.parser')
nav_bar = home_soup.find(class_= "nav-list")
for category in nav_bar.ul.findAll("a"):
    url_category = urljoin(home_url, category['href'])
    browse_category(url_category)

