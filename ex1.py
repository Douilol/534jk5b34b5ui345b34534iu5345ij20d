import json
import csv

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    data["data"] = [["reel", "imaginaire"]] + data["data"]
    print(data["data"])


with open("my.csv", "w", newline='', encoding="utf-8") as file_csv:
    file = csv.writer(file_csv, delimiter=',')
    for ligne in data["data"]:
        file.writerow(ligne)
