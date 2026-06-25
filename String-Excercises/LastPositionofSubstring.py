str1 = "Emma is a Emma data scientist who knows Emma Python. Emma works at a Emma google."
print(str1+"====is the INPUT STRING")
str = input("Enter a String:")
last_pos = str1.rfind(str)
print(f"Last Position of {str}:{last_pos}")
first_pos = str1.find(str)
print(f"First Position of {str}:{first_pos}")
pos=input("Which position required:")
pos=int(pos)-1
last_pos = str1.find(str,int(pos))
print(f"({pos}+1) Position of {str}:{last_pos}")

