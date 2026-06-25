inp=input("Enter your String:")
inp = inp.split(" ")
dictionary = {}
for i in inp:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i] = 1

print(dictionary)
