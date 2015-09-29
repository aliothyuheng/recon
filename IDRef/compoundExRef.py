
import csv

#import file
datafile = open('data_8.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

temp = []
result = []
idstring = []

for x in range(1, len(data)):
    if data[x][4] != '[]':
        if data[x][4] != '':
            temp.append("CheBI")
            temp.append(data[x][4])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
    if data[x][5] != '[]':
        if data[x][5] != '':
            if data[x][5].find(";") != -1:
                idstring = data[x][5].split(';')
                for y in range(0, len(idstring)):
                    temp.append("CheBI")
                    temp.append(idstring[y])
                    temp.append(x)
                    temp.append(0)
                    result.append(temp)
                    temp = []
            else:
                temp.append("CheBI")
                temp.append(data[x][5])
                temp.append(x)
                temp.append(0)
                result.append(temp)
                temp = []
                
    if data[x][6] != '[]':
        if data[x][6] != '':
            temp.append("KEGG")
            temp.append(data[x][6])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
    if data[x][7] != '[]':
        if data[x][7] != '':
            if data[x][7].find(";") != -1:
                idstring = data[x][7].split(';')
                for y in range(0, len(idstring)):
                    temp.append("KEGG")
                    temp.append(idstring[y])
                    temp.append(x)
                    temp.append(0)
                    result.append(temp)
                    temp = []
            else:
                temp.append("KEGG")
                temp.append(data[x][7])
                temp.append(x)
                temp.append(0)
                result.append(temp)
                temp = []
   
    if data[x][8] != '[]':
        if data[x][8] != '':
            temp.append("PubChem")
            temp.append(data[x][8])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
    if data[x][9] != '[]':
        if data[x][9] != '':
            if data[x][9].find(";") != -1:
                idstring = data[x][9].split(';')
                for y in range(0, len(idstring)):
                    temp.append("PubChem")
                    temp.append(idstring[y])
                    temp.append(x)
                    temp.append(0)
                    result.append(temp)
                    temp = []
            else:
                temp.append("PubChem")
                temp.append(data[x][9])
                temp.append(x)
                temp.append(0)
                result.append(temp)
                temp = [] 
    
    if data[x][10] != '[]':
        if data[x][10] != '':
            temp.append("HepatoNet")
            temp.append(data[x][10])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
           
    if data[x][11] != '[]':
        if data[x][11] != '':
            temp.append("EHMN")
            temp.append(data[x][11])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
    
    if data[x][12] != '[]':
        if data[x][12] != '':
            temp.append("HMDB")
            temp.append(data[x][12])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
    
    if data[x][13] != '[]':
        if data[x][13] != '':
            temp.append("LMSD")
            temp.append(data[x][13])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
    
    if data[x][14] != '[]':
        if data[x][14] != '':
            temp.append("InChi Key")
            temp.append(data[x][14])
            temp.append(x)
            temp.append(1)
            result.append(temp)
            temp = []
   
outfile = open('compoundExRef_1.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()


