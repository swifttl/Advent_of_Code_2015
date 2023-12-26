import re

input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2015/Day2/input2', 'r').read()
# print(input)
LWHregex = r'(\d+)x(\d+)x(\d+)'

# squareFeet = (2*l*w) + (2*w*h) + (2*h*l)
total = []
calc = 0
for x, y, z, in re.findall(LWHregex, input):
    l = int(x)
    w = int(y)
    h = int(z)
    sides= [l,w,h]
    smallestSide1 = min(sides)
    sides.remove(smallestSide1)
    smallestSide2 = min(sides)
    totalRibbon = (2*smallestSide1 + 2*smallestSide2) + (l*w*h)
    ribVol = l*w*h
    total.append(totalRibbon)

for i in total:
    calc+=i
print("The total amount of ribbon needed is:", calc)
