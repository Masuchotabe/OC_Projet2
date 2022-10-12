import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


def extract_book_data(url: str):
    """
    Extraction des données depuis la page web et transformation
    Args:
        url: URL de la page du livre

    Returns:
    Dict contenant les données tranformées du livre
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = re.sub(r'\([^)]+\)', "", soup.body.h1.string)
    product_information = soup.findAll(['td']) # récupération de la table product information
    nb_av = product_information[5].string # récupération du nombre de livre dispo
    nb_av = int(nb_av[nb_av.index("(") + 1:nb_av.index(")")].replace(" available", "").strip())
    category = soup.ul.findAll('li')[2].a.string
    description = soup.head.find(attrs={"name": "description"})['content'].strip()
    star_review = soup.find(class_="star-rating")["class"][1]
    img_url = urljoin(url, soup.find('img')["src"])
    extract_img(img_url, title)

    book_dict = {"product_page_url": url,
                 "universal_ product_code": product_information[0].string,
                 "title": title,
                 "price_including_tax": product_information[3].string,
                 "price_excluding_tax": product_information[2].string,
                 "number_available": nb_av,
                 "product_description": description,
                 "category": category,
                 "review_rating": star_review,
                 "image_url": img_url
                 }
    return book_dict


def extract_img(img_url: str, img_name: str):
    file_img = requests.get(img_url)
    path = "data/images"
    if not os.path.exists(path):
        os.makedirs(path)
    file_fullname = path + '/' + re.sub(r"[^_a-zA-Z0-9]", "", img_name.replace(" ", "_")) + ".jpg"
    with open(file_fullname, "wb") as file:
        file.write(file_img.content)
