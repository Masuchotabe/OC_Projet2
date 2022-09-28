import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/the-girl-you-left-behind-the-girl-you-left-behind-1_443/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
product_information = soup.findAll(['td'])
print(f'UPC = {product_information[0].string}')
print(f'price excl tax = {product_information[2].string}')
print(f'price incl tax = {product_information[3].string}')
nb_av = product_information[5].string
print(f'Availability = {nb_av[11:22]}')

category = soup.ul.findAll('li')[2].a.string
print(f'category = {category}')

desc = soup.head.find(attrs={"name": "description"})['content'].strip()
print(f'Description : {desc}')

star = soup.find(class_="star-rating")["class"][1]
print(star)

#print(type(product_information))
# print(soup.find('table'))
