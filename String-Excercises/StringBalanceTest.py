def string_balance(str1,str2):
    flag = True;
    for i in str1:
        if i in str2:
            continue
        else:
            flag = False
            break

    return flag


STR1 = input("Enter String to be Balanced Against:")
STR2 = input("Enter String to be Balanced:")



print("Is s1 and s2 balanced:",string_balance(STR1.lower(),STR2.lower()))


