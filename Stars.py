user_number = input('Enter a number: ')

try:
    user_input = int(user_number)
    for i in range(1,user_input+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
except ValueError:
    print(f'User input {user_number} is not a Number')