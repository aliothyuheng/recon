
import csv

#import file
datafile = open('IDRef.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

for x in range(1, len(data)):
    if data[x][3] == "[]":
        if data[x][1] != "[]":
            data[x][3] = data[x][1]

outfile = open('IdRef_v2.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(data)
outfile.close()


