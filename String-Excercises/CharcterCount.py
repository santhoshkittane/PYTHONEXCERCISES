from unicodedata import digit

str = input("Enter any String:")
alphabet = 0
digit = 0
symbol = 0

for i in str:
    if i.isalpha():
        alphabet+= 1
    elif i.isdigit():
        digit+=1
    else:
        symbol+=1


print(f"{str} has overall {len(str)} out of which {alphabet} alphabets, {digit} digits and {symbol} Symbols/Special Characters")