def average(num):
    total=0
    for i in num:
        total=total+i
    average_in = total/ len(num)
    return average_in

inp = input("Input any String containing numbers:")
num = []
for i in inp:
    if i.isdigit():
        num.append(int(i))
average = int(average(num))
print("The average is",average)
