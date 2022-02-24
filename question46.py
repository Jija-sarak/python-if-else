# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included).
number = int(input("enter a number:"))
if number>=1500 and number<=2700 :
    if number%7==0 and number%5==0:
        print("divisible by 7 and multiple of 5",number)
    # elif number%7==0:
    #     print("divisible by 7")
    # elif number%5==0:
    #     print("multiple of 5")
    else:
        print("not divisible by 7 and 5...")
else:
    print("enter right number")