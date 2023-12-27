input = open('input3pt1', 'r').read()

locationArray = [(0, 0)]
roboArray = [(0, 0)]
slocation = [0, 0]
rlocation = [0,0]

for i in range(len(input)):
    if i % 2 != 0:
        if input[i] == "^":
            slocation[1] += 1
        if input[i] == ">":
            slocation[0] += 1
        if input[i] == "<":
            slocation[0] -= 1
        if input[i] == "v":
            slocation[1] -= 1
        x = (slocation[0], slocation[1])
        locationArray.append(x)
    if i % 2 == 0:
        if input[i] == "^":
            rlocation[1] += 1
        if input[i] == ">":
            rlocation[0] += 1
        if input[i] == "<":
            rlocation[0] -= 1
        if input[i] == "v":
            rlocation[1] -= 1
        y = (rlocation[0], rlocation[1])
        locationArray.append(y)

print("The number of houses visited on the robo \n"
      "and Santa route that received at least one gift is:", len(set(locationArray)))
