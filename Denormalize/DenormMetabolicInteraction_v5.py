
import csv
   
datafile = open('DenormMetabolicInteraction_v4.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

for x in range(0, len(data)):
    if data[x][6] == "0":
        data[x][6] = "False"
    elif data[x][6] == "1":
        data[x][6] = "True"
        
outfile = open('DenormMetabolicInteraction_v5.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(data)
outfile.close()


