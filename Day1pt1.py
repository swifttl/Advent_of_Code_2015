input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2015/Day1/tester1', 'r').read()
print(input)
floor = 0
count = 0
for x in input:
    print(x)
    if x == "(":
        floor+=1
        count +=1

    elif x == ")":
        floor-=1
        count+=1
    if floor < 0:
        print(count)
        break

print(floor)