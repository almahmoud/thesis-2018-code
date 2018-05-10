import sys
from copy import deepcopy
import numpy as np
import csv

infilename = sys.argv[1]
outfilename = sys.argv[2]

inside = False
repeat = False
rows = []
currRow = []
curr = ""
lineNum = 0
colIndex = 0


keepCol = []
blocksCol = []
orderCol = 0
conditionCols = [0,0,0]
conditionTitles = ["PRIDE_IND","HAPPY_IND","SSR_IND"]
conditionNames = ["pride","happy","sr"]

tooFastLimit=0.0


print "Extracting information from input file"

with open(infilename, 'r') as csvfile:
    c = csvfile.read(1)
    while True:
        if c == '\n' and not inside:
            currRow.append(curr.strip('\r'))
            curr = ""
            colIndex = 0
            rows.append(deepcopy(currRow))
            currRow = []
            lineNum += 1
            c = csvfile.read(1)
        elif not c:
            break
        elif c == ',' and not inside:
            currRow.append(curr.strip('\r'))
            curr = ""
            colIndex += 1
            c = csvfile.read(1)
        elif c == '"' and not inside:
            inside = True
            c = csvfile.read(1)
        elif c == '"' and inside:
            nextc = csvfile.read(1)
            if nextc == '"':
                curr += str(nextc)
                c = csvfile.read(1)
            else:
                inside = False
                c = nextc
        else:
            curr += str(c)
            c = csvfile.read(1)

rowsInfo = [[] for i in range(len(rows))]

allResponseCol = []

print "Beginning column extraction"

for b in range(9):
    blockNum = b+1
    blockName = "Block" + str(blockNum)
    letterCol = []
    pressedCol = []
    responseCol = []
    typeCol = []
    keepCol = []
    for each in range(len(rows[0])):
        title = rows[0][each]
        if "Correct" in title and blockName in title:
            letterCol.append(each)
        elif "Response" in title and blockName in title:
            responseCol.append(each)
            allResponseCol.append(each)
        elif "Type" in title and blockName in title:
            typeCol.append(each)
        elif "Pressed" in title and blockName in title:
            pressedCol.append(each)
        elif title.count("Block") + title.count("Letter") == 0:
            keepCol.append(each)

        if "Block3Letter1Type" in title:
            orderCol = each
        for c in range(len(conditionTitles)):
            if conditionTitles[c] in title:
                conditionCols[c] = each

    blocksCol.append([deepcopy(letterCol),deepcopy(pressedCol),deepcopy(responseCol),deepcopy(typeCol)])

    prefix = "b"+str(blockNum)+"_"
    
    rowsInfo[0].append(prefix + "overall_cor_num")
    rowsInfo[0].append(prefix + "overall_cor_mean_res")

    rowsInfo[0].append(prefix + "overall_incor_num")
    rowsInfo[0].append(prefix + "overall_incor_mean_res")

    rowsInfo[0].append(prefix + "overall_nores_num")
    rowsInfo[0].append(prefix + "overall_toofast")
    rowsInfo[0].append(prefix + "overall_tooslow")

    
    rowsInfo[0].append(prefix + "g_cor_num")
    rowsInfo[0].append(prefix + "g_cor_mean_res")

    rowsInfo[0].append(prefix + "l_cor_num")
    rowsInfo[0].append(prefix + "l_cor_mean_res")

    rowsInfo[0].append(prefix + "g_incor_num")
    rowsInfo[0].append(prefix + "g_incor_mean_res")

    rowsInfo[0].append(prefix + "l_incor_num")
    rowsInfo[0].append(prefix + "l_incor_mean_res")

    rowsInfo[0].append(prefix + "g_nores_num")
    rowsInfo[0].append(prefix + "g_toofast")
    rowsInfo[0].append(prefix + "g_tooslow")

    rowsInfo[0].append(prefix + "l_nores_num")
    rowsInfo[0].append(prefix + "l_toofast")
    rowsInfo[0].append(prefix + "l_tooslow")

    rowsInfo[0].append(prefix + "switch_cor_num")
    rowsInfo[0].append(prefix + "switch_cor_mean_res")
    rowsInfo[0].append(prefix + "switch_incor_num")
    rowsInfo[0].append(prefix + "switch_incor_mean_res")
    rowsInfo[0].append(prefix + "switch_nores_num")
    rowsInfo[0].append(prefix + "switch_toofast")
    rowsInfo[0].append(prefix + "switch_tooslow")

    rowsInfo[0].append(prefix + "noswitch_cor_num")
    rowsInfo[0].append(prefix + "noswitch_cor_mean_res")
    rowsInfo[0].append(prefix + "noswitch_incor_num")
    rowsInfo[0].append(prefix + "noswitch_incor_mean_res")
    rowsInfo[0].append(prefix + "noswitch_nores_num")
    rowsInfo[0].append(prefix + "noswitch_toofast")
    rowsInfo[0].append(prefix + "noswitch_tooslow")


    rowsInfo[0].append(prefix + "ltog_cor_num")
    rowsInfo[0].append(prefix + "ltog_cor_mean_res")
    rowsInfo[0].append(prefix + "ltog_incor_num")
    rowsInfo[0].append(prefix + "ltog_incor_mean_res")
    rowsInfo[0].append(prefix + "ltog_nores_num")
    rowsInfo[0].append(prefix + "ltog_toofast")
    rowsInfo[0].append(prefix + "ltog_tooslow")
    
    rowsInfo[0].append(prefix + "gtol_cor_num")
    rowsInfo[0].append(prefix + "gtol_cor_mean_res")
    rowsInfo[0].append(prefix + "gtol_incor_num")
    rowsInfo[0].append(prefix + "gtol_incor_mean_res")
    rowsInfo[0].append(prefix + "gtol_nores_num")
    rowsInfo[0].append(prefix + "gtol_toofast")
    rowsInfo[0].append(prefix + "gtol_tooslow")
    

    rowsInfo[0].append(prefix + "gtog_cor_num")
    rowsInfo[0].append(prefix + "gtog_cor_mean_res")
    rowsInfo[0].append(prefix + "gtog_incor_num")
    rowsInfo[0].append(prefix + "gtog_incor_mean_res")
    rowsInfo[0].append(prefix + "gtog_nores_num")
    rowsInfo[0].append(prefix + "gtog_toofast")
    rowsInfo[0].append(prefix + "gtog_tooslow")

    
    rowsInfo[0].append(prefix + "ltol_cor_num")
    rowsInfo[0].append(prefix + "ltol_cor_mean_res")
    rowsInfo[0].append(prefix + "ltol_incor_num")
    rowsInfo[0].append(prefix + "ltol_incor_mean_res")
    rowsInfo[0].append(prefix + "ltol_nores_num")
    rowsInfo[0].append(prefix + "ltol_toofast")
    rowsInfo[0].append(prefix + "ltol_tooslow")


    rowsInfo[0].append(prefix + "first_three_all_mean_res")
    rowsInfo[0].append(prefix + "first_three_cor_num")
    rowsInfo[0].append(prefix + "first_three_cor_mean_res")
    rowsInfo[0].append(prefix + "first_three_incor_mean_res")
    rowsInfo[0].append(prefix + "first_three_no_res")
    rowsInfo[0].append(prefix + "fourth_res")
    rowsInfo[0].append(prefix + "last_res")


rowsInfo[0].append("Order")
rowsInfo[0].append("Condition")

for e in keepCol + allResponseCol:
    rowsInfo[0].append(rows[0][e])

if orderCol == 0:
    print "WARNING. Order column not detected (Block3Letter1Type)"

for cond in conditionCols:
    if cond == 0:
        "Warning: Condition columns not detected properly"


allResponses = [[] for a in range(len(blocksCol))]
limits = [[] for a in range(len(blocksCol))]

print "Beginning response times extraction"

for b in range(len(blocksCol)):

    block = blocksCol[b]
    responseCol = block[2]
    allResponses[b] = [[] for a in range(len(responseCol))]

for r in range(len(rows[1:])):

    row = rows[r+1]
    for b in range(len(blocksCol)):

        block = blocksCol[b]
        responseCol = block[2]

        currAllRes = allResponses[b]

        for i in range(len(responseCol)):
            entry = row[responseCol[i]]
            if entry != '' and 'N/A' not in entry and float(entry) > tooFastLimit:
                currAllRes[i].append(float(entry))

print "Calculating means and outlier limits"

for b in range(len(blocksCol)):

    block = blocksCol[b]
    responseCol = block[2]

    currAllRes = allResponses[b]

    for i in range(len(responseCol)):
        mean = np.mean(currAllRes[i])
        sd = np.std(currAllRes[i])
        upper = mean + 3*sd
        lower = mean - 3*sd
        limits[b].append([lower,upper])


print "Beginning caclulating each participant's data"
for r in range(len(rows[1:])):

    row = rows[r+1]

    rowRes = []

    for b in range(len(blocksCol)):
        block = blocksCol[b]
        letterCol = block[0]
        pressedCol = block[1]
        responseCol = block[2]
        typeCol = block[3]


        letters = []
        for i in letterCol:
            letters.append(row[i])

        pressed = []
        for i in pressedCol:
            pressed.append(row[i])

        responses = []
        for i in range(len(responseCol)):
            entry = row[responseCol[i]]
            limit = limits[b][i]
            if entry != '' and 'N/A' not in entry:
                if float(entry) < float(limit[0]) or float(entry) < tooFastLimit:
                    responses.append('N/A/fast')
                elif float(entry) > limit[1]:
                    responses.append('N/A/slow')
                else:
                    responses.append(entry)

            else:
                responses.append('N/A')

        rowRes.extend(responses)
        types = []
        for i in typeCol:
            types.append(row[i])

        if len(letters) != len(pressed) or len(pressed) != len(responses) or len(responses) != len(types):
            print "WARNING. The columns were extracted wrong"
            print letters
            print pressed
            print responses
            print types

        ## Info
        order = ""
        condition = ""
        ## responses
        ## types 
        allCorrect = []
        allIncorrect = []
        allNo = 0
        allTooFast = 0
        allTooSlow = 0

        globalCorrect = []
        localCorrect = []
        globalIncorrect = []
        localIncorrect = []

        switchCorrect = []
        switchIncorrect = []
        switchNo = 0
        switchTooFast = 0
        switchTooSlow = 0

        noswitchCorrect = []
        noswitchIncorrect = []
        noswitchNo = 0
        noswitchTooFast = 0
        noswitchTooSlow = 0

        localToGlobalCorrect = []
        localToGlobalIncorrect = []

        localToLocalCorrect = []
        localToLocalIncorrect = []

        globalToGlobalCorrect = []
        globalToGlobalIncorrect = []

        globalToLocalCorrect = []
        globalToLocalIncorrect = []

        globalNo = 0
        localNo = 0
        globalTooFast = 0
        globalTooSlow = 0
        localTooFast = 0
        localTooSlow = 0

        globalToLocalNo = 0
        localToGlobalNo = 0
        localToLocalNo = 0
        globalToGlobalNo = 0

        globalToLocalTooFast = 0
        localToGlobalTooFast = 0
        localToLocalTooFast = 0
        globalToGlobalTooFast = 0


        globalToLocalTooSlow = 0
        localToGlobalTooSlow = 0
        localToLocalTooSlow = 0
        globalToGlobalTooSlow = 0


        first3responses = []
        first3correct = []
        first3incorrect = []
        first3no = 0


        
        if "N/A" in responses[4]:
            fourthResponse = 99999.0
        else:
            fourthResponse = float(responses[4])

        
        if "N/A" in responses[len(responses) - 1]:
            lastResponse = 99999.0
        else:
            lastResponse = float(responses[len(responses) - 1])

        for i in range(len(letters)):
            if i < 3 and "N/A" not in responses[i]:
                if(responses[i] == '' or 'N/A' in responses[i]):
                    first3no +=1;
                else:
                    first3responses.append(float(responses[i]))
                    if pressed[i] == letters[i]:
                        first3correct.append(float(responses[i]))
                    else:
                        first3incorrect.append(float(responses[i]))


            if "N/A" in responses[i]:
                if "fast" in responses[i]:
                    if types[i] == "global":
                        globalTooFast += 1
                        if i>0 and types[i-1] == "local":
                            localToGlobalTooFast += 1

                        elif i > 0:
                            globalToGlobalTooFast += 1

                    elif types[i] == "local":
                        localTooFast += 1
                        if i>0 and types[i-1] == "global":
                            globalToLocalTooFast += 1

                        elif i > 0:
                            localToLocalTooFast += 1

                elif "slow" in responses[i]:
                    if types[i] == "global":
                        globalTooSlow += 1
                        if i>0 and types[i-1] == "local":
                            localToGlobalTooSlow += 1

                        elif i > 0:
                            globalToGlobalTooSlow += 1

                    elif types[i] == "local":
                        localTooSlow += 1
                        if i>0 and types[i-1] == "global":
                            globalToLocalTooSlow += 1

                        elif i > 0:
                            localToLocalTooSlow += 1
                
                else:
                    if types[i] == "global":
                        globalNo += 1
                        if i>0 and types[i-1] == "local":
                            localToGlobalNo += 1

                        elif i > 0:
                            globalToGlobalNo += 1

                    elif types[i] == "local":
                        localNo += 1
                        if i>0 and types[i-1] == "global":
                            globalToLocalNo += 1

                        elif i > 0:
                            localToLocalNo += 1

            if pressed[i] == letters[i]:
                if types[i] == "global":

                    if not (responses[i] == '' or 'N/A' in responses[i]):
                        globalCorrect.append(float(responses[i]))
                    if i>0 and types[i-1] == "local":

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            localToGlobalCorrect.append(float(responses[i]))
                    elif i > 0:

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            globalToGlobalCorrect.append(float(responses[i]))

                elif types[i] == "local":

                    if not (responses[i] == '' or 'N/A' in responses[i]):
                        localCorrect.append(float(responses[i]))
                    if i>0 and types[i-1] == "global":

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            globalToLocalCorrect.append(float(responses[i]))
                    elif i > 0:

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            localToLocalCorrect.append(float(responses[i]))

            else:
                if types[i] == "global":

                    if not (responses[i] == '' or 'N/A' in responses[i]):
                        globalIncorrect.append(float(responses[i]))
                    if i>0 and types[i-1] == "local":

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            localToGlobalIncorrect.append(float(responses[i]))
                    elif i > 0:

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            globalToGlobalIncorrect.append(float(responses[i]))

                elif types[i] == "local":

                    if not (responses[i] == '' or 'N/A' in responses[i]):
                        localIncorrect.append(float(responses[i]))
                    if i>0 and types[i-1] == "global":

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            globalToLocalIncorrect.append(float(responses[i]))
                    elif i > 0:

                        if not (responses[i] == '' or 'N/A' in responses[i]):
                            localToLocalIncorrect.append(float(responses[i]))


        allCorrect = globalCorrect + localCorrect
        allIncorrect = globalIncorrect + localIncorrect
        allNo = globalNo + localNo
        allTooFast = globalTooFast + localTooFast
        allTooSlow = globalTooSlow + localTooSlow

        rowsInfo[r+1].append(len(allCorrect))
        if len(allCorrect) > 0:
            rowsInfo[r+1].append(np.mean(allCorrect))
        else:
            rowsInfo[r+1].append(0)

        rowsInfo[r+1].append(len(allIncorrect))
        if len(allIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(allIncorrect))
        else:
            rowsInfo[r+1].append(0)

        rowsInfo[r+1].append(allNo)
        rowsInfo[r+1].append(allTooFast)
        rowsInfo[r+1].append(allTooSlow)



        rowsInfo[r+1].append(len(globalCorrect))
        if len(globalCorrect) > 0:
            rowsInfo[r+1].append(np.mean(globalCorrect))
        else:
            rowsInfo[r+1].append(0)

        rowsInfo[r+1].append(len(localCorrect))
        if len(localCorrect) > 0:
            rowsInfo[r+1].append(np.mean(localCorrect))
        else:
            rowsInfo[r+1].append(0)

        rowsInfo[r+1].append(len(globalIncorrect))
        if len(globalIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(globalIncorrect))
        else:
            rowsInfo[r+1].append(0)

        rowsInfo[r+1].append(len(localIncorrect))
        if len(localIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(localIncorrect))
        else:
            rowsInfo[r+1].append(0)

        rowsInfo[r+1].append(globalNo)
        rowsInfo[r+1].append(globalTooFast)
        rowsInfo[r+1].append(globalTooSlow)

        rowsInfo[r+1].append(localNo)
        rowsInfo[r+1].append(localTooFast)
        rowsInfo[r+1].append(localTooSlow)


        switchCorrect = globalToLocalCorrect + localToGlobalCorrect
        switchIncorrect = globalToLocalIncorrect + localToGlobalIncorrect
        switchNo = globalToLocalNo + localToGlobalNo
        switchTooFast = globalToLocalTooFast + localToGlobalTooFast
        switchTooSlow = globalToLocalTooSlow + localToGlobalTooSlow


        noswitchCorrect = localToLocalCorrect + globalToGlobalCorrect
        noswitchIncorrect = localToLocalIncorrect + globalToGlobalIncorrect
        noswitchNo = localToLocalNo + globalToGlobalNo
        noswitchTooFast = localToLocalTooFast + globalToGlobalTooFast
        noswitchTooSlow = localToLocalTooSlow + globalToGlobalTooSlow
        

        rowsInfo[r+1].append(len(switchCorrect))
        if len(switchCorrect) > 0:
            rowsInfo[r+1].append(np.mean(switchCorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(len(switchIncorrect))
        if len(switchIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(switchIncorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(switchNo)
        rowsInfo[r+1].append(switchTooFast)
        rowsInfo[r+1].append(switchTooSlow)




        rowsInfo[r+1].append(len(noswitchCorrect))
        if len(noswitchCorrect) > 0:
            rowsInfo[r+1].append(np.mean(noswitchCorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(len(noswitchIncorrect))
        if len(noswitchIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(noswitchIncorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(noswitchNo)
        rowsInfo[r+1].append(noswitchTooFast)
        rowsInfo[r+1].append(noswitchTooSlow)



        rowsInfo[r+1].append(len(localToGlobalCorrect))
        if len(localToGlobalCorrect) > 0:
            rowsInfo[r+1].append(np.mean(localToGlobalCorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(len(localToGlobalIncorrect))
        if len(localToGlobalIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(localToGlobalIncorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(localToGlobalNo)
        rowsInfo[r+1].append(localToGlobalTooFast)
        rowsInfo[r+1].append(localToGlobalTooSlow)
        
        rowsInfo[r+1].append(len(globalToLocalCorrect))
        if len(globalToLocalCorrect) > 0:
            rowsInfo[r+1].append(np.mean(globalToLocalCorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(len(globalToLocalIncorrect))
        if len(globalToLocalIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(globalToLocalIncorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(globalToLocalNo)
        rowsInfo[r+1].append(globalToLocalTooFast)
        rowsInfo[r+1].append(globalToLocalTooSlow)

        rowsInfo[r+1].append(len(globalToGlobalCorrect))
        if len(globalToGlobalCorrect) > 0:
            rowsInfo[r+1].append(np.mean(globalToGlobalCorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(len(globalToGlobalIncorrect))
        if len(globalToGlobalIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(globalToGlobalIncorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(globalToGlobalNo)
        rowsInfo[r+1].append(globalToGlobalTooFast)
        rowsInfo[r+1].append(globalToGlobalTooSlow)

        
        rowsInfo[r+1].append(len(localToLocalCorrect))
        if len(localToLocalCorrect) > 0:
            rowsInfo[r+1].append(np.mean(localToLocalCorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(len(localToLocalIncorrect))
        if len(localToLocalIncorrect) > 0:
            rowsInfo[r+1].append(np.mean(localToLocalIncorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(localToLocalNo)
        rowsInfo[r+1].append(localToLocalTooFast)
        rowsInfo[r+1].append(localToLocalTooSlow)

        if len(first3responses) > 0:
            rowsInfo[r+1].append(np.mean(first3responses))
        else:
            rowsInfo[r+1].append(0)

        rowsInfo[r+1].append(len(first3correct))
        if len(first3correct) > 0:
            rowsInfo[r+1].append(np.mean(first3correct))
        else:
            rowsInfo[r+1].append(0)
        if len(first3incorrect) > 0:
            rowsInfo[r+1].append(np.mean(first3incorrect))
        else:
            rowsInfo[r+1].append(0)
        rowsInfo[r+1].append(first3no)
        rowsInfo[r+1].append(fourthResponse)
        rowsInfo[r+1].append(lastResponse)

    for c in range(len(conditionCols)):
        if len(row[conditionCols[c]]) > 2:
            condition = conditionNames[c]
            
    if "global" in row[orderCol]:
        order = "global"
    elif "local" in row[orderCol]:
        order = "local"


    rowsInfo[r+1].append(order)
    rowsInfo[r+1].append(condition)

    
    for k in keepCol:
        rowsInfo[r+1].append(row[k])

    
    rowsInfo[r+1].extend(rowRes)


print "Writing to output file"

with open(outfilename, 'w') as out:
    writer = csv.writer(out, delimiter=',')
    for eachRow in rowsInfo:
        writer.writerow(eachRow)

        # for elem in eachRow[:-1]:
        #     out.write(elem)
        #     out.write(",")
        # out.write(eachRow[-1])
        # out.write("\n")

print "Successfully done"