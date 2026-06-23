def replace_char(str1, char):
    return str1.replace(char, "")
def count_char(str1, char):
    count = 0
    for i in str1:
        if i == char:
            count+=1
    return count


user_string = input("Enter a string: ")
char_to_remove = input("Enter a char to Remove: ")

if char_to_remove in user_string:
    # result = replace_char(user_string, char_to_remove)
    print(f"{char_to_remove} is present {count_char(user_string, char_to_remove)} times")
    print("After removing character:", replace_char(user_string, char_to_remove))
else:
    print(f"'{char_to_remove}' is not in the string")
