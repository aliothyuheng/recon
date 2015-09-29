
# coding: utf-8

# In[9]:

import csv

datafile = open('reaction.csv', 'r')
datareader = csv.reader(datafile)
reaction = []
for row in datareader:
    reaction.append(row)

temp = []
final = []

for x in range(1, len(reaction)):
    temp.append(reaction[x][4].split("="))


for x in range(0, len(temp)):
    print temp[x][0]
    temp[x][0] = temp[x][0].split("+")
    for y in range(0, len(temp[x][0])):
        temp[x][0][y] = temp[x][0][y].replace("<", "")
        temp[x][0][y] = temp[x][0][y].replace(">", "")
        if temp[x][0][y].startswith(" "):
            temp[x][0][y] = temp[x][0][y].replace(" ", "", 1)
        temp[x][0][y] = temp[x][0][y].rstrip()
    temp[x][1] = temp[x][1].split("+")
    for y in range(0, len(temp[x][1])):
        temp[x][1][y] = temp[x][1][y].replace("<", "")
        temp[x][1][y] = temp[x][1][y].replace(">", "")
        if temp[x][1][y].startswith(" "):
            temp[x][1][y] = temp[x][1][y].replace(" ", "", 1)
        temp[x][1][y] = temp[x][1][y].rstrip()

outfile = open('reaction_comparison.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(final_result)
outfile.close()      
        

