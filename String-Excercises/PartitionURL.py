input = input("Enter any Email Address:")
FName = input.partition("@")[0].partition(".")[0]
Lname = input.partition("@")[0].partition(".")[2]
print("Name:", FName+" "+Lname)
CompanyName = input.partition("@")[2].partition(".")[0]
print("Company:", CompanyName)
