
# coding: utf-8

# In[1]:

#create compound external reference from new compound data
import csv
new_cpd = {}
with open("Compound_Data_v2.04.csv", "rb") as f:
    f.next()
    reader = csv.reader(f)
    for line in reader:
        new_cpd[line[0]] = line[1:]
f.close()

#match cpd abbreviation to cpd id
cpd_id = {}
with open("Compound.csv") as f:
    f.next()
    reader = csv.reader(f)
    for line in reader:
        cpd_id[line[2]] = line[0]
f.close()   

#metNames,metHMDB,metKeggID,metEHMNID,metFormulas,metCHEBIID,metPubChemID,metHepatoNetID,metInchiString,metCharge,b,c
ExRef = []
i = 1
for cpd_abbr, cpd_id in cpd_id.items():
    cpd_info = new_cpd[cpd_abbr]
    if len(cpd_info[1]) > 0:
        ExRef.append([i, "HMDB", cpd_info[1], cpd_id, 0])
        i += 1
    if len(cpd_info[2]) > 0:
        ExRef.append([i, "KEGG", cpd_info[2], cpd_id, 0])
        i += 1
    if len(cpd_info[3]) > 0:
        ExRef.append([i, "EHMN", cpd_info[3], cpd_id, 0])
        i += 1
    if len(cpd_info[5]) > 0:
        ExRef.append([i, "CHEBI", cpd_info[5], cpd_id, 0])
        i += 1
    if len(cpd_info[6]) > 0:
        ExRef.append([i, "PubChem", cpd_info[6], cpd_id, 0])
        i += 1
    if len(cpd_info[7]) > 0:
        ExRef.append([i, "HepatoNet", cpd_info[7], cpd_id, 0])
        i += 1

with open("compoundExRef_v2.0.4.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(ExRef)
f.close()

