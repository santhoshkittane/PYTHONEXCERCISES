def vowel_counter(Str1):
    count = 0
    Vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in Str1:
        if i in Vowel:
            count += 1
    return count

# Vowel = ['a,'e,'i','o','u','A','E','I','O','U']
input = input("Enter String:")
print("Total number of vowels:",vowel_counter(input))