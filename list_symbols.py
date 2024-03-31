import csv

with open('symbols.csv') as input: 
    reader = csv.reader(input)
    reader.__next__()
    
    for row in reader:
        print(row)