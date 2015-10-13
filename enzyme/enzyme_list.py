import csv

#import file
datafile = open('Enzyme.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)    
for x in range(0, len(data)):
    data[x][1] = data[x][1].replace("'", "")

datafile = open('enzclass.csv', 'r')
datareader = csv.reader(datafile)
enz = []
for row in datareader:
    enz.append(row)  
list_1 = []
list_2 = []
list_3 = []
for x in range(10, len(enz)):
    if enz[x] != []:
        if enz[x][0].find('-') == 3:
            list_1.append(enz[x][0])
        if enz[x][0].find('-') == 6:
            list_2.append(enz[x][0])
        if enz[x][0].find('-') == 8:
            list_3.append(enz[x][0])

for x in range(0, len(list_1)):
    list_1[x] = list_1[x].split('.')
for x in range(0, len(list_2)):
    list_2[x] = list_2[x].split('.')
for x in range(0, len(list_3)):
    list_3[x] = list_3[x].split('.')
for x in range(0, len(list_1)):
    list_1[x][3] = list_1[x][3].replace('-', '')
for x in range(0, len(list_2)):
    list_2[x][1] = list_2[x][1].replace(' ', '')
    list_2[x][3] = list_2[x][3].replace('-', '')
for x in range(0, len(list_3)):
    list_3[x][1] = list_3[x][1].replace(' ', '')
    list_3[x][2] = list_3[x][2].replace(' ', '')
    list_3[x][3] = list_3[x][3].replace('-', '')


temp = []
str = ''
result = []
for x in range(1, len(data)):
    temp = data[x][1].split('.')
    for a in range(0, len(list_1)):
        if temp[0] == list_1[a][0]:
            str = str + list_1[a][3] + ','
    for b in range(0, len(list_2)):
        if temp[0] == list_2[b][0]:
            if temp[1] == list_2[b][1]:
                str = str + list_2[b][3] + ','
    for c in range(0, len(list_3)):
        if temp[0] == list_3[c][0]:
            if temp[1] == list_3[c][1]:
                if temp[2] == list_3[c][2]:
                    str = str + list_3[c][3]
    result.append(str)
    str = ''

outfile = open('enzyme_list.csv', 'wb')
writer = csv.writer(outfile)
writer.writerow(result)
outfile.close()

