import csv

#import file
datafile = open('reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

temp = []
for x in range(0, len(data)):
    temp.append(data[x][5])

result = list(set(temp))

outfile = open('pathway.csv', 'wb')
writer = csv.writer(outfile)
writer.writerow(result)
outfile.close()



