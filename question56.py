# Write a Python program to change a given string to a new 
# string where the first and last chars have been exchanged.
string = input("enter a string:")
if len(string)>0:
    print(string[-1:]+string[1:len(string)-1]+string[:1])
else:
    print("check your code")
    