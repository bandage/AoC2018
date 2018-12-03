with open('d2INPUT.txt', 'r') as inputFile:
        data = inputFile.read()

# break string into list
data = data.split()

#TEST DATA
#data =['abcd','aabc','abab']

#count the number of occurances of each letter
def countDuplicates(inp):
	x = {}
	for i in inp:
		x.setdefault(i,0)
		x[i] += 1
	return x

charTally = {}

for id in data:
    charTally[id] = countDuplicates(id)

twoCounter = 0

def counter(dict_in,count_val):
    valCounter = 0
    for key,values in charTally.items():
        for v in values.values():   # the dictonary values wihtin the dictionary values
            if int(v) == count_val:
                valCounter += 1
                break  #stop it from looking for futher instances of count_val
    return valCounter
    
Alg_1 = counter(charTally,2)
Alg_2 = counter(charTally,3)

Ans = Alg_1 * Alg_2

print(Ans)
    
#part 2

import Levenshtein
Ans =''

while Ans=='':
    for id in data:
        a = id
        for id2 in data:
            if Levenshtein.distance(a,id2) == 1:
                Ans= str(a)
                Ans2=str(id2)
                break
            if Ans=='':
                continue
        if Ans=='':
            continue
output = ''
for i in range(len(Ans)):
    if Ans[i] == Ans2[i]:
        output += Ans[i]

print(output)
