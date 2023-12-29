import re
input = open('input6', 'r').read().split('\n')

def on():
    if 'on' in instr:
        for i in range(sY, fY + 1):
            lst = [*x[i]]
            for j in range(sX, fX + 1):
                lst[j] = '-'
            x[i] = ''.join(lst)
def off():
    if 'off' in instr:
        for i in range(sY, fY + 1):
            lst = [*x[i]]
            for j in range(sX, fX + 1):
                lst[j] = 'O'
            x[i] = ''.join(lst)
def toggle():
    if 'toggle' in instr:
        for i in range(sY, fY + 1):
            lst = [*x[i]]
            for j in range(sX, fX + 1):
                if lst[j] == 'O':
                    lst[j] = '-'
                elif lst[j] == '-':
                    lst[j] = 'O'
            x[i] = ''.join(lst)

rows, col = (1000,1000)
x = [''.join(["O"]*col)]*rows

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

sum = 0
for line in x:
    sum+=line.count('-')
print("The number of lights on is:",sum)