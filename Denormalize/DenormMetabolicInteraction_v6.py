
import csv
   
datafile = open('DenormMetabolicInteraction_v5.csv', 'r')
datareader = csv.reader(datafile)
data = []
for row in datareader:
    data.append(row)

for x in range(0, len(data)):
    if data[x][5].isdigit() == False:
        data[x][5] = "NULL"
        
outfile = open('DenormMetabolicInteraction_v6.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(data)
outfile.close()


