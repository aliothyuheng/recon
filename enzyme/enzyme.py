import csv

#import file
datafile = open('reaction_list.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

temp = []
for x in range(1, len(data)):
    string = data[x][12]
    if string != "":
        temp.append(string)

result = list(set(temp))

outfile = open('Enzyme.csv', 'wb')
writer = csv.writer(outfile)
writer.writerow(result)
outfile.close()



