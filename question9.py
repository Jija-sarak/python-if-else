# Write a python program to input any character and check whether it is alphabet, digit or special character.
user_input = input("enter a character:")
if user_input >= "a" and user_input<= "z" or user_input>= "A" and user_input<= "Z":
    print("it is alphabet")
elif user_input >= "0" and user_input < "9":
    print("it is digit")
else :
    print("it is special character") 