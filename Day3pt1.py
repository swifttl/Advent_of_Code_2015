input = open('input3pt1', 'r').read()
print(input)

locationArray = [(0, 0)]
location = [0, 0]
for i in range(len(input)):
    if input[i] == "^":
        location[1] += 1
    if input[i] == ">":
        location[0] += 1
    if input[i] == "<":
        location[0] -= 1
    if input[i] == "v":
        location[1] -= 1
    x = (location[0], location[1])
    locationArray.append(x)

print("The number of houses that received at least one gift is:", len(set(locationArray)))
