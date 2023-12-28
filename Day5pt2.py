input = open('input5', 'r').read().splitlines()
niceArray = []


def skipcheck(line):
    niceORnaughty = "naughty"
    for ch in range(len(line[:-2])):
        if line[ch] == line[ch+2]:
            niceORnaughty = "nice"
    if niceORnaughty == "nice":
        return True
    else:
        return False

def paircheck(line):
    pairArray = []
    for ch in range(len(line[:-1])):
        posPair = line[ch]+line[ch+1]
        if line.count(posPair) >= 2:
            pairArray.append(posPair)
    if len(pairArray) != 0:
        return True
    else:
        return False


for i in input:
    line = i
    if skipcheck(line) == True and paircheck(line) == True:
        niceArray.append(line)

print("The number of nice strings is:", len(niceArray))