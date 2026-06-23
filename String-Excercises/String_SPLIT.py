str1 = "Emma,is,a,data,scien tist"
str1 = str1.split(',')
print(str1)
for i in str1:
    print(i)
    if " " in i:
        i = i[::-1]
        print(i)

print("Final:::::::::::::::")
