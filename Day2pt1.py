import re

input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2015/Day2/input2', 'r').read()
# print(input)

LWHregex = r'(\d+)x(\d+)x(\d+)'
total = []
calc = 0
for x, y, z, in re.findall(LWHregex, input):
    l = int(x)
    w = int(y)
    h = int(z)
    squareFeet = (2 * l * w) + (2 * w * h) + (2 * h * l)
    smallestSide = min([l*w, w*h, l*h])
    total.append(squareFeet+smallestSide)

for i in total:
    calc+=i
print("The total amount of wrapping paper needed is:", calc)
