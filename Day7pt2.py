import re
input = open('input7','r').read().splitlines()
values = {}
linesplitRegex = r'\s->\s'
starters = []

#Create dictionary of variables and rules
for line in input:
    rules,name = re.split(linesplitRegex, line)
    rul = rules.split()
    values[name] = rul

#New input from Part 1
values['b'] = ['3176']

#In the dictionary, turn assigned values into integers and create array to make subs
for key in values:
    if len(values[key]) ==1 and values[key][0].isdigit():
        num = int(values[key][0])
        values[key] = num
        starters.append(key)

#In the list of rules, find any digits and turn them into integers
for key in values:
    if isinstance(values[key], list):
        for i in values[key]:
            if i.isdigit():
                values[key][values[key].index(i)] = int(i)

#Make subs for all known values
for s in starters:
    for key in values:
        if isinstance(values[key], list) and s in values[key]:
            values[key][values[key].index(s)] = values[s]


while values['a'] == ['lx']:
    for key in values:
        try:
            if isinstance(values[key], list) and "AND" in values[key]:
                values[key] = values[key][0] & values[key][2]
            elif isinstance(values[key], list) and "OR" in values[key]:
                values[key] = values[key][0] | values[key][2]
            elif isinstance(values[key], list) and "LSHIFT" in values[key]:
                values[key] = values[key][0] << values[key][2]
            elif isinstance(values[key], list) and "RSHIFT" in values[key]:
                values[key] = values[key][0] >> values[key][2]
            elif isinstance(values[key], list) and "NOT" in values[key]:
                values[key] = 65535 - values[key][1]
            if isinstance(values[key], int) and key not in starters:
                starters.append(key)
                s = key
                for key in values:
                    if isinstance(values[key], list) and s in values[key]:
                        values[key][values[key].index(s)] = values[s]
                    starters.clear()
        except TypeError:
            pass
values['a'] = int(values['a'][0])
print('The new values of each circuit is:', values)
print("The new value of 'a' in the circuit is:", values['a'])
