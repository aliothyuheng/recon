import csv

#import file
datafile = open('reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

temp = []
for x in range(0, len(data)):
    if data[x][8] != "''":
        temp.append(data[x][8])

temp_1 = []
result = []
for x in range(0, len(temp)):
    if temp[x].find("or") != -1:
        temp_1 = temp[x].split("or")
        for y in range(0, len(temp_1)):
            result.append(temp_1[y])
        temp_1 = []
    else:
        result.append(temp[x])
result_1 = []
result_2 = []
for x in range(0, len(result)):
    if result[x].find("and") != -1:
        result_1 = result[x].split("and")
        for y in range(0, len(result_1)):
            result_2.append(result_1[y])
        result_1 = []
    else:
        result_2.append(result[x])
for x in range(0, len(result_2)):
    result_2[x] = result_2[x].replace("'", "")
    result_2[x] = result_2[x].replace(" ", "")
    result_2[x] = result_2[x].replace("(", "")
    result_2[x] = result_2[x].replace(")", "")
for x in range(0, len(result_2)):
    result_2[x] = result_2[x][:-2]

result_final = list(set(result_2))

outfile = open('gene.csv', 'wb')
writer = csv.writer(outfile)
writer.writerow(result_final)
outfile.close()


