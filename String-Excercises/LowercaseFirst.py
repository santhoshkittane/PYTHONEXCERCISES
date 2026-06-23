
def conversion(str1):
    lower = ""
    upper = ""
    for i in str1:
        if i.islower():
            lower = lower+i
        else:
            upper = upper+i
    return lower+upper
input= input("Enter String:")
print("After Conversion:",conversion(input))

