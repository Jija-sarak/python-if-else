# Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.
string = input("enter a string")
if string[:2]=="Is":
    print(string)
else:
    print("Is "+string)