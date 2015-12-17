
# coding: utf-8

# In[1]:

#add metref to id Ex Ref
import csv
refmet = {}
with open("refmet_100515.csv", "rb") as f:
    f.next()
    reader = csv.reader(f)
    for line in reader:
        refmet[line[5]] = line[9]
f.close()

i = 1
result = []
exclude = []
with open("compoundExRef_v2.0.4.csv", "rb") as f:
    reader = csv.reader(f)
    for line in reader:
        temp = []
        temp.append(i)
        if line[1] != "PubChem":
            temp.extend(line[1:])
            result.append(temp)
            i += 1
        else:
            temp.extend(line[1:])
            pubchem = line[2]
            result.append(temp)
            i += 1
            temp = []
            temp.append(i)
            met = refmet.get(pubchem,0)
            if met == 0:
                exclude.append(pubchem)
            else:
                temp.append("RefMet")
                temp.append(met)
                temp.extend(line[3:])
                result.append(temp)
                i += 1

with open("compoundExRef_v2.0.4_v2.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(result)
f.close()

with open("compoundWithoutRefmet.csv", "wb") as f:
    for item in exclude:
        f.write(item)
        f.write("\n")
f.close()

