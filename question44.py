# Accept three numbers from the user and display the second largest number.
num = int(input("enter a number:"))
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
# if num>num2 and num<num1 or num<num2 and num>num1:
#     print("second largest number :",num)
# elif num1>num2 and num>num1 or num1<num2 and num<num1:
#     print("second largest number :",num1)
# else:
#     print("second largest number :",num2)
if num > num1 and num > num2:
    print(num)
elif num1>num2 and num1 > num:
    print(num1)
elif num2 > num and num2 > num1:
    print(num2)
else:
    print("second largest number")