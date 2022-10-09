import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from extract import extract_book_data
from store_data import store_in_csv
import pprint

pp = pprint.PrettyPrinter(sort_dicts=False)

url_category = "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"

page = requests.get(url_category)
soup = BeautifulSoup(page.content, 'html.parser')
data = []
next_page = soup.find(class_="next")
# Récupération de toutes les données de la page
for tag in soup.findAll('article'):
    url = urljoin(url_category, tag.a['href'])
    # print(url)
    data_temp = extract_book_data(url)
    # pp.pprint(data_temp)
    data.append(data_temp)

#pp.pprint(data)
store_in_csv('test.csv', data)
#
# url = "http://books.toscrape.com/catalogue/the-perfect-play-play-by-play-1_352/index.html"
# data = extract_book_data(url)
#
#
# pp.pprint(data)
