
# coding: utf-8

# In[1]:

import csv

#import file
datafile = open('reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

compoundfile = open('compound.csv', 'r')
datareader = csv.reader(compoundfile)
compound = []
for row in datareader:
    compound.append(row)
temp = []
for x in range(1, len(data)):
    temp.append(data[x][2].split("="))
    
for x in range(0, len(temp)):
    temp[x][0] = temp[x][0].replace(">" , "")
    temp[x][0] = temp[x][0].replace("<" , "")
    temp[x][1] = temp[x][1].replace(">" , "")
    temp[x][1] = temp[x][1].replace("<" , "")
    temp[x][0] = temp[x][0].split("+")
    temp[x][1] = temp[x][1].split("+")
    
    
left_temp = []
right_temp = []
left = []
right = []
for x in range(0, len(temp)):
    for y in range(0, len(temp[x][0])):
        if temp[x][0][y].startswith(" "):
            temp[x][0][y] = temp[x][0][y].replace(" ", "", 1)
        temp[x][0][y] = temp[x][0][y].rstrip()
        if temp[x][0][y] != "":
            if temp[x][0][y].find(" ") != -1:
                temp[x][0][y] = temp[x][0][y].split(" ")
                left_temp.append(str(x+1))
                left_temp.append(temp[x][0][y][1])
                left_temp.append(temp[x][0][y][0])
                left.append(left_temp)
                left_temp = []
            else:
                left_temp.append(str(x+1))
                left_temp.append(temp[x][0][y])
                left_temp.append("1")
                left.append(left_temp)
                left_temp = []
        else:
            left_temp.append(str(x+1))
            left_temp.append("")
            left.append(left_temp)
            left_temp = []
    for y in range(0, len(temp[x][1])):
        if temp[x][1][y].startswith(" "):
            temp[x][1][y] = temp[x][1][y].replace(" ", "", 1)
        temp[x][1][y] = temp[x][1][y].rstrip()
        if temp[x][1][y] != "":
            if temp[x][1][y].find(" ") != -1:
                temp[x][1][y] = temp[x][1][y].split(" ")
                right_temp.append(str(x+1))
                right_temp.append(temp[x][1][y][1])
                right_temp.append(temp[x][1][y][0])
                right.append(right_temp)
                right_temp = []
            else:
                right_temp.append(str(x+1))
                right_temp.append(temp[x][1][y])
                right_temp.append("1")
                right.append(right_temp)
                right_temp = []
        else:
            right_temp.append(str(x+1))
            right_temp.append("")
            right.append(right_temp)
            right_temp = []

inputresult = []
outputresult = []
tempresult = []
for x in range(0, len(left)):
    if left[x][1] != '':
        tempresult.append(left[x][0])
        tempresult.append(left[x][1])
        for y in range(0, len(compound)):
            if left[x][1] == compound[y][2]:
                tempresult.append(compound[y][0])
        tempresult.append(left[x][2])
        inputresult.append(tempresult)
        tempresult = []
    else:
        tempresult.append(left[x][0])
        tempresult.append(left[x][1])
        inputresult.append(tempresult)
        tempresult = []


for x in range(0, len(right)):
    if right[x][1] != '':
        tempresult.append(right[x][0])
        tempresult.append(right[x][1])
        for y in range(0, len(compound)):
            if right[x][1] == compound[y][2]:
                tempresult.append(compound[y][0])
        tempresult.append(right[x][2])
        outputresult.append(tempresult)
        tempresult = []
    else:
        tempresult.append(right[x][0])
        tempresult.append(right[x][1])
        outputresult.append(tempresult)
        tempresult = []
    

outfile = open('reaction2input.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(inputresult)
outfile.close()
outfile = open('reaction2output.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(outputresult)
outfile.close()


# In[ ]:



