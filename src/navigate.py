import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from extract import extract_book_data


def browse_category(url_category: str):
    """
    Récupère tous les liens des livres présent dans la catégorie
    Args:
        url_category: url de la categorie a browser

    Returns:
        data : list des dictinnaires avec données de tous les livres de la catégorie

    """

    data = []
    urls = []

    # Récupération de toutes les données de la page
    while True:
        page = requests.get(url_category)
        soup = BeautifulSoup(page.content, 'html.parser')
        for tag in soup.findAll('article'):
            urls.append(urljoin(url_category, tag.a['href']))

        next_page = soup.find(class_="next")

        if next_page is None:
            break
        else:
            url_category = urljoin(url_category, next_page.a['href'])

    if len(urls) > 0:
        for url in urls:
            data.append(extract_book_data(url))
        return data


def get_category_urls(url: str):
    """
    Récupère les urls de toutes les catégories du site
    Args:
        url: url de la page d'accueil du site

    Returns:
        urls_category : list contenant les urls de chaque catégorie
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    nav_bar = soup.find(class_="nav-list")
    urls_category = []
    for tag in nav_bar.ul.findAll("a"):
        urls_category.append(urljoin(url, tag['href']))
    return urls_category
