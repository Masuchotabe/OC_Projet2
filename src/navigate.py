import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from extract import extract_book_data
from store_data import store_in_csv


def browse_category(url_category: str):
    page = requests.get(url_category)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = []
    print(f"categorie : {url_category}")

    # Récupération de toutes les données de la page
    while True:
        for tag in soup.findAll('article'):
            url = urljoin(url_category, tag.a['href'])
            print(f"url = {url}")
            data_temp = extract_book_data(url)
            data.append(data_temp)

        next_page = soup.find(class_="next")

        if next_page is None:
            break
        else:
            url_category = urljoin(url_category, next_page.a['href'])
            page = requests.get(url_category)
            soup = BeautifulSoup(page.content, 'html.parser')
            print(url_category)

    store_in_csv(data)
