import os

from json import loads
from datetime import datetime
from pprint import pprint


source = "../docs"
allowed = ".json"
mandatory = ["items"]
currency = "$"


def get_data():
    """ Load all the json files from the source directory """
    files = os.listdir(source)
    result = list()
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == allowed:
            with open(os.path.join(source, file), "r+") as f:
                formatted = {
                    "file_name": file,
                    "data": loads(f.read())
                }
            result.append(formatted)
    return result


def get_total(items: list, file_name):
    """ Compute the total spend for each json file """
    total = 0
    for item in items:
        try:
            total += int(item["value"]) * (int(item["quantity"])
                                           if "quantity" in item else 1)
        except:
            raise BaseException(
                f"[EXCEPTION] - value is missing of not a number file: {file_name}")
    return total


def parse():
    """ Returns the data loaded from the json files in a standard format """
    file_data = get_data()

    return [{
        "file_name": file["file_name"],
        "date": (file["date"] if "date" in file else datetime.now().strftime("%d/%m/%Y")),
        "category": (file["data"]["category"] if "category" in file["data"] else "other"),
        "total": f"{get_total(file['data']['items'], file['file_name'])}{currency}"
    } for file in file_data]

if __name__ == "__main__":
    parsed = parse()
    pprint(parsed)