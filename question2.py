# maximum between tree numbers 
num = int(input("enter a number:"))
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
if num > num1 and num > num2:
    print("maximum number is",num)
elif num1 > num and num1 > num2:
     print("maximum number is",num1)
else:
     print("maximum number is",num2)
