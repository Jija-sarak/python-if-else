# Write a python program to input the month number and print the number of days in that month.
user_input = int(input("enter a number"))
if user_input == 2:
    print("in this month there are 28/29 days")
elif user_input < 8 and user_input % 2==0 or user_input == 9 or user_input==11:
        print("30 days in a month")
else:
    print("31 days in month")









