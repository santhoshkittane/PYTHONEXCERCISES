inp = input("Input any String Value:")
dictionary = dict()
for i in list(inp):
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)
