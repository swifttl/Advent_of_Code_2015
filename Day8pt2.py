import re

input = open('input8','r').read().splitlines()

totalSum = []
addedSum = []
slashRegex = r'\\'
quoteRegex = r'"'

for line in input:
    totalChar = 0
    for i in line:
        totalChar+=1
    numSlash = len(re.findall(slashRegex, line))
    numQuote = len(re.findall(quoteRegex, line))
    allChar = totalChar + numQuote + numSlash  + 2
    totalSum.append((allChar))
    addedSum.append(allChar - (numQuote + numSlash  + 2))

calSum = 0
for i in range(len(totalSum)):
    calSum += (totalSum[i]-addedSum[i])

print('The number of all coded characters is:', calSum)
