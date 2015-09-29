
# coding: utf-8

# In[2]:

import csv
   
datafile = open('DenormMetabolicInteraction_v6.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

datafile = open('compoundExRef_1.csv', 'r')
datareader = csv.reader(datafile)
ref = []
for row in datareader:
    ref.append(row)
    
datafile = open('compound.csv', 'r')
datareader = csv.reader(datafile)
cpd = []
for row in datareader:
    cpd.append(row)

for x in range(0, len(data)):
    for y in range(0, len(cpd)):
        if data[x][1] == cpd[y][2]:
            data[x][1] = cpd[y][0]

hasID = False
for x in range(0, len(data)):
    for y in range(0, len(ref)):
        if data[x][1] == ref[y][3] and ref[y][1] == "KEGG" and ref[y][4] == "1":
            data[x][1] = ref[y][2]
            hasID = True
        if data[x][1] == ref[y][3] and ref[y][1] == "EHMN" and ref[y][4] == "1":
            data[x][1] = ref[y][2]
            hasID = True
    if hasID == False:
        data[x][1] = "[]"
    hasID = False
    
outfile = open('DenormMetabolicInteraction_v7.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(data)
outfile.close()   


# In[3]:




# In[ ]:



