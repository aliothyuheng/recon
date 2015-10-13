import csv

#import file
datafile = open('reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

enzymefile = open('enzyme.csv', 'r')
datareader = csv.reader(enzymefile)
enzyme = []
for row in datareader:
    enzyme.append(row)

temp = []
result = []

for x in range(0, len(data)):
    if data[x][12] != "":
        for y in range(1, len(enzyme)):
            if enzyme[y][1] == data[x][12]:
                temp.append(x)
                temp.append(enzyme[y][0])
                result.append(temp)
                temp = []
                
outfile = open('reaction2enzyme.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()
