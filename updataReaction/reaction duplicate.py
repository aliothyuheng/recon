#this file is to remove the duplicate reactions from the reaction table and the other tables related to reaction
import csv
data = []
#data import
with open("ReactionEquation.csv", "rb") as f:
    reader = csv.reader(f)
    for line in reader:
        if int(line[0]) % 2 == 0:
            data.append(line[2:])
            
result_dic = {}
for line in data:
    if result_dic.get(line[0], 0) == 0:
        result_dic[line[0]] = line[1]
    else:
        temp = result_dic[line[0]]
        temp = temp + " , " + line[1]
        result_dic[line[0]] = temp        

#old_id, new_id reference        
i = 1
result = []
for k, v in result_dic.items():
    result.append([i, v, k])
    i += 1
    
with open("reaction_ref.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(result)
f.close()

#read reaction ref
ref = {}
with open("reaction_ref.csv", "rb") as f:
    reader = csv.reader(f,  quotechar='"')
    for line in reader:
        temp = line[1].split(",")
        ref[line[0]] = temp
f.close()

#read reaction file
reaction = {}
with open("Reaction_v2.csv","rb") as f:
    reader = csv.reader(f, quotechar='"')
    for line in reader:
        reaction[line[0]] = line[1:]
f.close()

#new reaction result to new_result list
new_result = []
for k, v in ref.items():
    new_id = k
    old_ids = v
    reaction_id = []
    reverse = []
    sourse = 0
    for old_id in old_ids:
        old_reaction_info = reaction[old_id.strip()]
        if old_reaction_info[0] not in reaction_id:
            reaction_id.append(old_reaction_info[0])
        if old_reaction_info[1] not in reverse:
            reverse.append(old_reaction_info[1])
    new_reaction_info = [k, ",".join(reaction_id), ",".join(reverse), sourse]
    new_result.append(new_reaction_info)    

with open("reaction_v2_remove_duplicate.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(new_result)
f.close()

#update the reaction equation table
equation = {}
with open("reactionEquation.csv", "rb") as f:
    reader = csv.reader(f, quotechar='"')
    for line in reader:        
        if equation.get(line[3], 0) == 0:
            temp = {}
            temp[line[1]] = line[2]
            equation[line[3]] = temp
        else:
            temp = equation[line[3]]
            temp[line[1]] = line[2]
            equation[line[3]] = temp
f.close()    

'''
with open("reactionEquation_remove_duplicate_v1.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(new_equation)
f.close()
'''

#remove location within reaction
import re
i = 1
new_equation = []
for k, v in ref.items():
    new_id = k
    old_ids = v
    name = equation[v[0].strip()]["NAME"]
    abbr = equation[v[0].strip()]["ABBR"]
    abbr = re.sub(r'\[.*?\]', '', abbr)
    new_equation.append([i, "ABBR", abbr, k])
    i += 1
    new_equation.append([i, "NAME", name, k])
    i += 1    

with open("reactionEquation_remove_duplicate_v2.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(new_equation)
f.close()


import csv
#read reaction ref
ref = {}
with open("reaction_ref.csv", "rb") as f:
    reader = csv.reader(f,  quotechar='"')
    for line in reader:
        temp = line[1].split(",")
        ref[line[0]] = temp
f.close()

#update reaction to location
position = {}
with open ("reaction2Location.csv", "rb") as f:
    reader = csv.reader(f, quotechar='"')
    for line in reader:
        if position.get(line[0], 0) == 0:
            position[line[0]] = [line[1]]
        else:
            position[line[0]].append(line[1])
f.close()
new_location = []
for k, v in ref.items():
    new_id = k
    old_ids = v
    old_location = []
    for old_id in old_ids:
        if old_id != "old_id":
            temp_position = position[old_id.strip()]
            if temp_position not in old_location:
                old_location.extend(temp_position)
        temp = [k, " , ".join(list(set(old_location)))]
        new_location.append(temp)

with open("reaction2Loacation_remove_duplication.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(new_location)
f.close()

#update reaction to pathway
ref = {}
with open("reaction_ref.csv", "rb") as f:
    reader = csv.reader(f,  quotechar='"')
    for line in reader:
        temp = line[1].split(",")
        ref[line[0]] = temp
f.close()

pathway = {}
with open ("reaction2Pathway.csv", "rb") as f:
    reader = csv.reader(f, quotechar='"')
    for line in reader:
        pathway[line[0]] = line[1]
f.close()

#remove transport reaction
transport_list =  ["17","29","39","48","64","65","77"]
transport_id = "101"
new_pathway = []
for k, v in ref.items():
    new_id = k
    old_ids = v
    old_pathway = []
    for old_id in old_ids:
        temp_pathway = pathway[old_id.strip()]
        if temp_pathway in transport_list:
            if transport_id not in old_pathway:
                old_pathway.append(transport_id)
        elif temp_pathway not in old_pathway:
            old_pathway.append(temp_pathway)
    temp = [k, " , ".join(old_pathway)]
    new_pathway.append(temp)
    
with open("reaction2Pathway_remove_duplication.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(new_pathway)
f.close()


# In[ ]:




# In[ ]:



