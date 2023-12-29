import re
input = open('input6', 'r').read().split('\n')

def on():
    if 'on' in instr:
        for i in range(sY, fY + 1):
            for j in range(sX, fX + 1):
                x[i][j]+=1
def off():
    if 'off' in instr:
        for i in range(sY, fY + 1):
            for j in range(sX, fX + 1):
                x[i][j]-=1
                if x[i][j] < 0:
                    x[i][j] = 0
def toggle():
    if 'toggle' in instr:
        for i in range(sY, fY + 1):
            for j in range(sX, fX + 1):
                x[i][j]+=2


##Couldnt use system of joining and editing list, had to create initial array a different way.
##This system would have probably been easier for Part 1, using 0/1 as on/off rather than O/-.
###Would have avoid all the issues with strings. May rewrite Part 1 to test
x =[]
xRow= []
rows, col = range(0,1000), range(0,1000)
for i in rows:
    xRow = []
    for i in col:
        xRow.append(0)
    x.append(xRow)


dirRegex = r'(turn on |toggle |turn off )(\d+),(\d+) through (\d+),(\d+)'
a=0

for line in input:
    for instr, b, c, d, e in re.findall(dirRegex, line):
        sX = int(b)
        sY = int(c)
        fX = int(d)
        fY = int(e)
        dx = fX - sX
        dy = fY - sY
        on()
        off()
        toggle()

calSum = 0
for line in x:
    for i in line:
        calSum+=i
print("The total brightness is:",calSum)