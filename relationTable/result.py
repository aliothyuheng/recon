
import csv

#import file
datafile = open('F:\\ID-new\\primary database\\reaction2input_1.csv', 'r')
datareader = csv.reader(datafile)
data_1 = []
for row in datareader:
    data_1.append(row)

reactionfile = open('F:\\ID-new\\primary database\\enzyme2reaction2gene.csv', 'r')
datareader = csv.reader(reactionfile)
reaction = []
for row in datareader:
    reaction.append(row)

datafile = open('F:\\ID-new\\primary database\\reaction2output_1.csv', 'r')
datareader = csv.reader(datafile)
data_2 = []
for row in datareader:
    data_2.append(row)
    
temp = []
result = []
number = 1

for x in range(1, len(data_1)):
    temp.append(number)
    number += 1
    temp.append(data_1[x][2])
    temp.append(data_1[x][1])
    temp.append("in")
    for y in range(1, len(reaction)):
        if data_1[x][1] == reaction[y][2]:
            temp.append(reaction[y][1])
            temp.append(reaction[y][3])
    if len(temp) != 6:
        temp.append("")
        temp.append("")
    result.append(temp)
    temp = []
    
    
for x in range(1, len(data_2)):
    temp.append(number)
    number += 1
    temp.append(data_2[x][2])
    temp.append(data_2[x][1])
    temp.append("out")
    for y in range(1, len(reaction)):
        if data_2[x][1] == reaction[y][2]:
            temp.append(reaction[y][1])
            temp.append(reaction[y][3])
    if len(temp) != 6:
        temp.append("")
        temp.append("")
    result.append(temp)
    temp = []

outfile = open('F:\\ID-new\\primary database\\result.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()




