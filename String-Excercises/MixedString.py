from typing import final


def stringmix(str1,str2):
    final=""
    S1_length=len(str1)
    S2_length=len(str2)
    str2=str2[::-1]
    length = S1_length if S1_length>S2_length else S2_length
    for i in range(length):
        if i<S1_length:
            final+=str1[i]
        if i<S2_length:
            final+=str2[i]
    return final


str1 = input("Input any String Value:")
str2 = input("Input another String Value:")
print("Final String is ",stringmix(str1,str2))