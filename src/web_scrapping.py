from store_data import store_in_csv
from navigate import browse_category, get_category_urls


home_url = "http://books.toscrape.com/index.html"
# récupération des url de catégorie
urls_category = get_category_urls(home_url)
# pour chaque catégrorie on browse et récupère les data de chaque livre qu'on met en csv ensuite
for url in urls_category:
    books_data = browse_category(url)
    store_in_csv(books_data)
