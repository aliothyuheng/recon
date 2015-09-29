
import csv
datafile = open('IDRef_old.csv', 'r')
datareader = csv.reader(datafile)
old_idref = []
for row in datareader:
    old_idref.append(row)

datafile = open('IDRef_v2.csv', 'r')
datareader = csv.reader(datafile)
idref = []
for row in datareader:
    idref.append(row)

temp = []
result = []
for x in range(1, len(idref)):
    temp.append(idref[x][0])
    temp.append(idref[x][2])
    for y in range(0, len(old_idref)):
        if idref[x][2] == old_idref[y][0]:
            temp.append(old_idref[y][1])
    result.append(temp)
    temp = []

outfile = open('IDRef_v3.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()


