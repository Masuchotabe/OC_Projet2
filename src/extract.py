import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from transform import transform_data
from store_data import store_img


def extract_book_data(url: str):
    """
    Extraction des données depuis la page web et appelle transform_data pour transformer les données en dict
    Extraction de l'image et stockage
    Args:
        url: URL de la page du livre

    Returns:
    Dict contenant les données tranformées du livre
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.body.h1.string
    product_information = soup.findAll(['td']) # récupération de la table product information
    category = soup.ul.findAll('li')[2].a.string
    description = soup.head.find(attrs={"name": "description"})['content']
    star_review = soup.find(class_="star-rating")["class"][1]
    img_url = urljoin(url, soup.find('img')["src"])

    data_clean, img_name = transform_data(url, title, product_information, description, category, star_review, img_url)

    img = requests.get(img_url)  # stockage de l'image
    store_img(img.content, img_name, data_clean["category"])

    return data_clean


