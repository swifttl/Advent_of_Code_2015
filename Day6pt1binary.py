import re
input = open('input6', 'r').read().split('\n')

def on():
    if 'on' in instr:
        for i in range(sY, fY + 1):
            for j in range(sX, fX + 1):
                x[i][j] = 1
def off():
    if 'off' in instr:
        for i in range(sY, fY + 1):
            for j in range(sX, fX + 1):
                x[i][j] = 0
def toggle():
    if 'toggle' in instr:
        for i in range(sY, fY + 1):
            for j in range(sX, fX + 1):
                if x[i][j] == 0:
                    x[i][j] = 1
                elif x[i][j] == 1:
                    x[i][j] = 0


### Rework from orig using binary instead of strings. Way easier. Still would like a cleaner way to create
### initial array that can be edited.
### rows, col = (1000,1000) -- x = [[0]*col]*rows edits each column of each row rather than individual indices
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
print("The number of lights on is:",calSum)