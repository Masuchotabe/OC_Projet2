import csv
import os


def store_in_csv(content: []):
    if len(content) > 0:
        header = list(content[0].keys())
        # print(f"header = {header}")
    path = "data/csv"
    category_name = content[0]["category"]
    if not os.path.exists(path):
        os.makedirs(path)
    file_fullname = path + "/" + category_name + ".csv"
    with open(file_fullname, 'w', newline='', encoding="utf-8") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=header, delimiter=";", quoting=csv.QUOTE_MINIMAL)

        writer.writeheader()
        for elm in content:
            writer.writerow(elm)
            # print(f"ligne : {elm}")
