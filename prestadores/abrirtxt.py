import csv

with open('procedencia.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)