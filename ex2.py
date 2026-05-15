import csv
import json

with open("poke.csv", newline='') as f:
    filecsv = csv.reader(f)
    for ligne in filecsv:
        mylist = []
        for i in range (1, 7):
            mylist.append(int(ligne[i].split(",")[0]))
        print(f"{ligne[0].split(",")[0]}: {mylist}")


    #{ }