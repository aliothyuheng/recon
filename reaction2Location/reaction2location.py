
# coding: utf-8

# In[1]:

import csv

#import file
datafile = open('F:\\ID-new\\reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

locationfile = open('F:\\ID-new\\database\\location_1.csv', 'r')
datareader = csv.reader(locationfile)
location = []
for row in datareader:
    location.append(row)
    
temp = []
result = []

for x in range(1, len(data)):
    for y in range(1, len(location)):
        if data[x][2].find(location[y][1]) != -1:
            temp.append(x)
            temp.append(location[y][0])
            result.append(temp)
            temp = []

outfile = open('F:\\ID-new\\database\\reaction2location_1.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()

