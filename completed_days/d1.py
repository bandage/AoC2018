with open('d1INPUT.txt','r') as inputFile:
        data = inputFile.read()

# break string into list
data = data.split()

# create holding variable
output = 0

# cycle though the list and add each to the output var
def addFrequency(fList):
    global output
    for i in fList:
        output += int(i)
    return output

a = addFrequency(data)
print('Total is '+ str(a))

# part 2
output = 0
freqCount = {}
while 2 not in freqCount.values():
    for i in data:
        output += int(i)
        if output in freqCount:
            print('first doubled frequency is ' + str(output))
            freqCount[output] += 1
            break
        else:
            freqCount[output] = 1
    if 2 not in freqCount.values():
        continue
       
   
