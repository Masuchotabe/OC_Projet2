import csv
import os


def store_in_csv(content: []):
    """
    Ecris les données dans un fichier csv pour une categorie complete
    Args:
        content: list de dictionnaire à mettre dans le ccsv


    """
    if len(content) > 0:
        header = list(content[0].keys())

        category_name = content[0]["category"]
        path = "data/"+str(category_name)
        if not os.path.exists(path):
            os.makedirs(path)
        file_fullname = path + "/" + category_name + ".csv"
        with open(file_fullname, 'w', newline='', encoding="utf-8") as csv_file:

            writer = csv.DictWriter(csv_file, fieldnames=header, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)

            writer.writeheader()
            for elm in content:
                writer.writerow(elm)


def store_img(img_content, img_name, category):
    """
    enregistre l'image dans le sous dossier data/ avec le nom de catégorie
    Args:
        img_content: fichier img
        img_name: nom de l'image
        category: nom du dossier de catégorie

    Returns:

    """
    path = "data/" + str(category) + "/img"
    if not os.path.exists(path):
        os.makedirs(path)
    file_fullname = path + '/' + img_name + ".jpg"

    with open(file_fullname, "wb") as file:
        file.write(img_content)
