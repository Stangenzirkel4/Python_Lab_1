import csv

#Открываем на чтение
with open('books.csv') as f:
    reader = csv.DictReader(f, delimiter=';')

