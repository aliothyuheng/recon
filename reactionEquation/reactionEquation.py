
import csv

#import file
datafile = open('reaction.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

num = 1
temp = []
result = []
for x in range(1, len(data)):
    temp.append(num)
    temp.append("ABBR")
    temp.append(data[x][4])
    temp.append(data[x][0])
    result.append(temp)
    temp = []
    num = num + 1
    temp.append(num)
    temp.append("NAME")
    temp.append(data[x][5])
    temp.append(data[x][0])
    result.append(temp)
    temp = []
    num = num + 1
        
outfile = open('ReactionEquation.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()


