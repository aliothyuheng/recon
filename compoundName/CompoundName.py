
# coding: utf-8

# In[4]:

import csv
#This is a program intended to exact the primary compound name and synonym from the original table

#import file
datafile = open('compound.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

num = 1
temp = []
result = []
#if the fifth column is empty, then the compound does not have synonym
for x in range(1, len(data)):
    if data[x][4] == '[]':
        temp.append(num)
        temp.append(data[x][3])
        temp.append("primary")
        temp.append(data[x][0])
        result.append(temp)
        temp = []
        num = num + 1
    else:
        temp.append(num)
        temp.append(data[x][3])
        temp.append("primary")
        temp.append(data[x][0])
        result.append(temp)
        temp = []
        num = num + 1
        temp.append(num)
        temp.append(data[x][4])
        temp.append("synonym")
        temp.append(data[x][0])
        result.append(temp)
        temp = []
        num = num + 1

#output to the compoundName file
outfile = open('CompoundName.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()
        


# In[ ]:



