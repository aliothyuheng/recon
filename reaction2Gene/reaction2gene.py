import csv

#import file
datafile = open('reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

enzymefile = open('gene.csv', 'r')
datareader = csv.reader(enzymefile)
gene = []
for row in datareader:
    gene.append(row)
temp = []
result = []
tempgene = ''
for x in range(1, len(data)):
    if data[x][8] != "''":
        if data[x][8] != "'":
            for y in range(1, len(gene)):
                tempid = gene[y][1] + ".1"
                if data[x][8].find(tempid) != -1:
                    temp.append(x)
                    temp.append(gene[y][0])
                    result.append(temp)
                    temp = []

outfile = open('reaction2gene.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()



