#author: @shannonmcdermitt
import csv

# print CSV as list
with open('love.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)