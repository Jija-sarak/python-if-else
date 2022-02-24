# Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
number = int(input("enter a number:"))
number=number%10
if number%3==0:
    print(number,"divisible")
else:
    print(number,"not divisible")
