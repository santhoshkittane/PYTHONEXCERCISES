STR1 = input("Enter your Sentence:")
Find = input("Enter String to be searched:")
count = STR1.lower().count(Find.lower())

print(f"{Find} has occured {count} times")