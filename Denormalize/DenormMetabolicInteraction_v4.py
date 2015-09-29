
import csv

#import file
datafile = open('Compound.csv', 'r')
datareader = csv.reader(datafile)
compound = []
for row in datareader:
    compound.append(row)

datafile = open('Reaction.csv', 'r')
datareader = csv.reader(datafile)
reaction = []
for row in datareader:
    reaction.append(row)
    
datafile = open('DenormMetabolicInteraction_v3.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

for x in range(0, len(data)):
    for y in range(0, len(compound)):
        if data[x][1] == compound[y][0]:
            data[x][1] = compound[y][2]
    for y in range(0, len(reaction)):
        if data[x][2] == reaction[y][0]:
            data[x][2] = reaction[y][1]

outfile = open('DenormMetabolicInteraction_v4.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(data)
outfile.close()


