# Write a program to check whether a number entered is a three digit number or not.
num = int(input("enter a number:"))
if num>=100 and num<=999:
    print(num,"It is a three digit number")
else:
    print(num,"It is not a three digit number")
