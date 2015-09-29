
# coding: utf-8

# In[3]:

import csv

#import file
datafile = open('compound2reaction_final_v2.csv', 'r')
datareader = csv.reader(datafile)
reaction = []
for row in datareader:
    reaction.append(row)

datafile = open('relationTable.csv', 'r')
datareader = csv.reader(datafile)
relation = []
for row in datareader:
    relation.append(row)

num = 1
for x in range(1, len(reaction)):
    for y in range(0, len(relation)):
        if reaction[x][0] == relation[y][1] and reaction[x][2] == relation[y][2] and reaction[x][8] == relation[y][4]:
            reaction[x][6] = relation[y][3]
            reaction[x][5] = relation[y][5]

outfile = open('DenormMetabolicInteraction_v2.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(reaction)
outfile.close()


# In[ ]:



