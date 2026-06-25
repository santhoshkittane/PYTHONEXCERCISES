inp = input("Enter your String:")
inp = inp.split()
res = []
# for item in inp:
#     if any(char.isalpha() for char in item) and if(char.isdigit() for char in item):
for item in inp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
length=len(res)
if length>0:
    print(f"Overall {length} has numbers in it and the are below")
    print(res)
else:
    print(f"No number and character mix strings present")