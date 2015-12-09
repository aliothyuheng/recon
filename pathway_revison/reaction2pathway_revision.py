#seperate transport pathway
import csv
pathway = []
with open("Pathway.csv", "rb") as f:
    reader = csv.reader(f, quotechar='"')
    for line in reader:
        pathway.append(line)
f.close()

#remove transport pathway and reassign pathway id
new_pathway = []
transport = []

for i in xrange(len(pathway)):
    temp = []
    if "Transport" in pathway[i][1]:
        temp.append(transport_num)
        transport.append(pathway[i])
    else:
        new_pathway.append(pathway[i])

new_pathway.append([int(pathway[-1][0])+1, "Transport", "NULL", ""])

with open("pathway_transport.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(transport)
f.close()

with open("pathway_remove_transport.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(new_pathway)
f.close()

