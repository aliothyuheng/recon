import csv
#find the reaction with duplicate pathway
duplicate_pathway = []
with open("reaction2Pathway_remove_duplication.csv", "rb") as f:
    reader = csv.reader(f)
    for line in reader:
        if "," in line[1]:
            duplicate_pathway.append(line[0])
f.close()

#read reaction ref
ref = {}
with open("reaction_ref.csv", "rb") as f:
    reader = csv.reader(f)
    for line in reader:
        temp = line[1].split(",")
        ref[line[0]] = temp
f.close()

#read pathway ref
pathway = {}
with open("pathway_remove_transport.csv", "rb") as f:
    reader = csv.reader(f)
    for line in reader:
        pathway[line[1]] = line[0]
f.close()

#read original file
original = []
with open("reaction original.csv", "rb") as f:
    reader = csv.reader(f)
    for line in reader:
        original.append(line)
f.close()

#pull all the reaction with multiple pathways out of the original reaction table
result = []
for item in duplicate_pathway:
    reaction = ref[item]
    for i in reaction:
        temp = []
        temp.append(item)
        temp.append(i)
        temp.extend(original[int(i)][:3])
        path = original[int(i)][3].replace("'", "")
        if "Transport" in path:
            temp.append("101")
        else:
            temp.append(pathway[path])
        result.append(temp)
        
with open("reaction_pathway_duplicate.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(result)
f.close()