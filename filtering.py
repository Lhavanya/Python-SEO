import re
import csv

myFile = open('historietas.txt', 'r')

yourResult = [line.split('[') for line in myFile.readlines()]

for lst in yourResult:
    for j, item in enumerate(lst):
        lst[j] = item.replace('-', '').replace(']', '')

for line in range(len(yourResult)):
     yourResult[line][1] = yourResult[line][1].split('/', 1)[0].replace(".","")


with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(yourResult)

