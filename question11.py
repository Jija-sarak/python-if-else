# Write a python program to input week number and print week day.
user_input = int(input("enter a week number:"))
if user_input == 1:
    print("Monday")
elif user_input == 2:
    print("Tuesday")
elif user_input == 3:
    print("Wednesday")
elif user_input == 4:
    print("Thursday")
elif user_input == 5:
    print("Friday")
elif user_input == 6:
    print("Saturday")
elif user_input == 7:
    print("Sunday")
else:
    print("enter a number between 1 to 7")
