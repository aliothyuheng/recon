
# coding: utf-8

# In[2]:

import csv

#import file
datafile = open('reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

pathwayfile = open('pathway.csv', 'r')
datareader = csv.reader(pathwayfile)
pathway = []
for row in datareader:
    pathway.append(row)
temp = []
result = []

for x in range(1, len(data)):
    for y in range(1, len(pathway)):
        if data[x][5] == pathway[y][1]:
            temp.append(x)
            temp.append(pathway[y][0])
            result.append(temp)
            temp = []

outfile = open('reaction2pathway.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()

