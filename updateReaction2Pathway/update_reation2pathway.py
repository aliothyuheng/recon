
# coding: utf-8

# In[2]:

#this file is to update the reaction2pathway file
import csv
pathway = {}
with open("reaction_pathway_duplicate_v2.csv", "rb") as f:
    f.next()
    reader = csv.reader(f)
    for line in reader:
        if pathway.get(line[0], 0) == 0:
            pathway[line[0]] = line[5]
f.close()

result = []
with open("reaction2pathway_remove_duplication.csv", "rb") as f:
    reader = csv.reader(f)
    for line in reader:
        if "," not in line[1]:
            result.append(line)
f.close()

for k,v in pathway.items():
    temp = [k,v]
    result.append(temp)
    
with open("reaction2pathway_remove_duplication_v2.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(result)
f.close()

