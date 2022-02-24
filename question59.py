# Write a Python program which accepts the user's first and last name and print them in reverse order
#  with a space between them .
# Input1: kumar 
# Input 2:nayak
# Output: nayak kumar
first_name = input("enter your name:")
last_name = input("enter your surname:")
if first_name != last_name:
    print(last_name,first_name)
else:
    print(first_name,last_name)