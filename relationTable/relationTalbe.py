
import csv

#import file
datafile = open('F:\\ID-new\\primary database\\result.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

number = 1
temp_1 = []
temp_2 = []
result = []
temp = []
final = []
for x in range(0, len(data)):
    if data[x][4] != "":
        if data[x][4].find("or") != -1:
            temp_1 = data[x][4].split("or")
        for y in range(0, len(temp_1)):
            if temp_1[y].find("and") != -1:
                temp_2 = temp_1[y].split("and")
                for z in range(0, len(temp_2)):
                    result.append(temp_2[z])
            else:
                result.append(temp_1[y])
        temp_1 = []
        temp_2 = []
        for w in range(0, len(result)):
            result[w] = result[w].replace("(", "")
            result[w] = result[w].replace(")", "")
            result[w] = result[w].replace(" ", "")
            result[w] = result[w].replace("'", "")
            result[w] = result[w][:-2]
            temp.append(number)
            number += 1
            temp.append(data[x][0])
            temp.append(data[x][1])
            temp.append(data[x][2])
            temp.append(data[x][3])
            temp.append(result[w])
            print temp
            temp = []
    else:
        temp.append(number)
        number += 1
        temp.append(data[x][0])
        temp.append(data[x][1])
        temp.append(data[x][2])
        temp.append(data[x][3])
        temp.append(data[x][4])
        final.append(temp)
        print temp
        temp = []
    result = []

outfile = open('F:\\ID-new\\primary database\\relationTable.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(final)
outfile.close()


