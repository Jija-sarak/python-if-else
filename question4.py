# Write a python program to check whether a number is divisible by 5 and 11 or not.
num = int(input("enter a number:"))
if num % 5 == 0 and num % 11 == 0 :
    print("divisible by both")
elif num % 5 == 0 :
    print("divisible by 5")
elif num % 11 == 0 :
    print("divisible by 11")
else:
    print("not divisible")
