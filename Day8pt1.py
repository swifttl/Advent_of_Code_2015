import re
totalSum = []
escapedSum = []
input = open('input8','r').read().splitlines()

hexRegex = r'\\x\w+'
slashRegex = r'\\\\'
quoteRegex = r'\\"'
workaround = r'\\\\x\w+'
workaround2 = r'\\\\\\x\w+'
for line in input:
    totalChar = 0
    addedChar = 0
    for i in line:
        totalChar+=1
    numHex = len(re.findall(hexRegex, line)) - len(re.findall(workaround, line)) + len(re.findall(workaround2, line))
    numSlash = len(re.findall(slashRegex, line))
    numQuote = len(re.findall(quoteRegex, line[:-1]))
    escapedChar = totalChar -(numQuote + numSlash + (numHex * 3) + 2)
    escapedSum.append(escapedChar)
    totalSum.append((totalChar))

calSum = 0
for i in range(len(totalSum)):
    calSum += (totalSum[i]-escapedSum[i])

print('The number of escaped characters is:', calSum)



