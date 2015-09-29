
import csv

#import file
datafile = open('compound2reaction.csv', 'r')
datareader = csv.reader(datafile)
reaction = []
for row in datareader:
    reaction.append(row)

datafile = open('comparison_v7.csv', 'r')
datareader = csv.reader(datafile)
comparison = []
for row in datareader:
    comparison.append(row)
    
datafile = open('IDRef_v3.csv', 'r')
datareader = csv.reader(datafile)
reference = []
for row in datareader:
    reference.append(row)

datafile = open('reaction2input.csv', 'r')
datareader = csv.reader(datafile)
cpdInput = []
for row in datareader:
    cpdInput.append(row)

datafile = open('reaction2output.csv', 'r')
datareader = csv.reader(datafile)
cpdOutput = []
for row in datareader:
    cpdOutput.append(row)

for x in range(0, len(cpdInput)):
    if cpdInput[x][1] == "":
        for y in range(0, len(cpdOutput)):
            if cpdInput[x][0] == cpdOutput[y][0]:
                cpdInput[x][1] = cpdOutput[y][1]
                cpdInput[x].append(cpdOutput[y][2])
                cpdInput[x].append(cpdOutput[y][3])

for x in range(0, len(cpdOutput)):
    if cpdOutput[x][1] == "":
        for y in range(0, len(cpdInput)):
            if cpdOutput[x][0] == cpdInput[y][0]:
                cpdOutput[x][1] = cpdInput[y][1]
                cpdOutput[x].append(cpdInput[y][2])
                cpdOutput[x].append(cpdInput[y][3])


result = []
temp = []
hasincome = False
for x in range(0, len(comparison)):
    if comparison[x][1] == "0":
        for y in range(0, len(cpdInput)):
            if comparison[x][0] == cpdInput[y][0]:
                temp.append(cpdInput[y][2])
                temp.append("0")
                temp.append(cpdInput[y][0])
                temp.append("0")
                temp.append("1")
                temp.append("1")
                temp.append("in")
                result.append(temp)
                temp = []
        for y in range(0, len(cpdOutput)):
            if comparison[x][0] == cpdOutput[y][0]:
                temp.append(cpdOutput[y][2])
                temp.append("0")
                temp.append(cpdOutput[y][0])
                temp.append("0")
                temp.append("1")
                temp.append("1")
                temp.append("out")
                result.append(temp)
                temp = []
    elif comparison[x][1] != "'":
        for y in range(0, len(cpdInput)):
            if comparison[x][0] == cpdInput[y][0]:
                for z in range(0, len(reference)):
                    if cpdInput[y][2] == reference[z][0]: 
                        for w in range(0, len(reaction)):
                            if comparison[x][1] == reaction[w][1] and reference[z][2] == reaction[w][0]:
                                temp.append(cpdInput[y][2])
                                temp.append(reference[z][2])
                                temp.append(cpdInput[y][0])
                                temp.append(comparison[x][1])
                                temp.append(reaction[w][2])
                                temp.append(reaction[w][3])
                                temp.append("in")
                                result.append(temp)
                                temp = []
        for y in range(0, len(cpdOutput)):
            if comparison[x][0] == cpdOutput[y][0]:
                for z in range(0, len(reference)):
                    if cpdOutput[y][2] == reference[z][0]: 
                        for w in range(0, len(reaction)):
                            if comparison[x][1] == reaction[w][1] and reference[z][2] == reaction[w][0]:
                                temp.append(cpdOutput[y][2])
                                temp.append(reference[z][2])
                                temp.append(cpdOutput[y][0])
                                temp.append(comparison[x][1])
                                temp.append(reaction[w][2])
                                temp.append(reaction[w][3])
                                temp.append("out")
                                result.append(temp)
                                temp = []
    else:
        for y in range(0, len(cpdInput)):
            if comparison[x][0] == cpdInput[y][0]:
                temp.append(cpdInput[y][2])
                temp.append("NULL")
                temp.append(cpdInput[y][0])
                temp.append("NULL")
                temp.append(cpdInput[y][3])
                temp.append("1")
                temp.append("in")
                result.append(temp)
                temp = []
        for y in range(0, len(cpdOutput)):
            if comparison[x][0] == cpdOutput[y][0]:
                temp.append(cpdOutput[y][2])
                temp.append("NULL")
                temp.append(cpdOutput[y][0])
                temp.append("NULL")
                temp.append(cpdOutput[y][3])
                temp.append("1")
                temp.append("out")
                result.append(temp)
                temp = []
        


outfile = open('compound2reaction_final_v2.csv', 'wb')
writer = csv.writer(outfile)
writer.writerows(result)
outfile.close()
    




