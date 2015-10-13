import csv

#import file
datafile = open('compound.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

locationfile = open('location.csv', 'r')
datareader = csv.reader(locationfile)
location = []
for row in datareader:
    location.append(row)

temp = []
result = []
    
for x in range(1, len(data)):
    temp.append(data[x][0])
    str = data[x][2]
    str = str[-3::]
    for y in range(1, len(location)):
        if str == location[y][1]:
           temp.append(location[y][0])
    result.append(temp)
    temp = []

outfile = open('compound2location.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()




