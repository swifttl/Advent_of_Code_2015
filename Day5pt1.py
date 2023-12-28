input = open('input5', 'r').read().splitlines()
vowelArray = ['a', 'e', 'i', 'o', 'u',]
forbiddenArray = ['ab', 'cd', 'pq', 'xy']
niceArray = []

def vowelCheck(line):
    vList = []
    for ch in range(len(line)):
        if line[ch] in vowelArray:
            vList.append(line[ch])
    if len(vList)>2:
        return True
    else:
        return False

def forbidCheck(line):
    naughtyORnice = "nice"
    for i in forbiddenArray:
        if i in line:
            naughtyORnice = "naughty"
    if naughtyORnice == "nice":
        return True
    else:
        return False

def doubleCheck(line):
    niceORnaughty = "naughty"
    for ch in range(len(line[:-1])):
        if line[ch] == line[ch+1]:
            niceORnaughty = "nice"
    if niceORnaughty == "nice":
        return True
    else:
        return False

for i in input:
    line = i
    if forbidCheck(line) == True and doubleCheck(line) == True and vowelCheck(line) == True:
        niceArray.append(line)

print("The number of nice strings is:", len(niceArray))