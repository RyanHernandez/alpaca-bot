import csv

header = 'Symbol'
inputFile = 'nasdaq.csv'
with open(inputFile) as input: 
    reader = csv.reader(input)
    firstLetter = 'A'
    for row in reader:
        outputFile = 'data/symbols/' + firstLetter + '_symbols.csv'
        with open(outputFile, 'a', newline='') as output:
            writer = csv.writer(output)
            if row[0] == "Symbol":
                continue
            writer.writerow([row[0]])
            firstLetter = row[0][0].capitalize()
            outputFile = 'data/symbols/' + firstLetter + '_symbols.csv'