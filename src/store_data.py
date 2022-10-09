import csv
import os


def store_in_csv(file_name: str, content: []):
    if len(content) > 0:
        header = list(content[0].keys())
        # print(f"header = {header}")
    path = "data/csv"
    if not os.path.exists(path):
        os.makedirs(path)
    file_fullname = path + "/test.csv"
    with open(file_fullname, 'w', newline='') as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=header)
        # TODO verifier le delimiter / dialect
        writer.writeheader()
        for elm in content:
            writer.writerow(elm)
            #print(f"ligne : {elm}")
