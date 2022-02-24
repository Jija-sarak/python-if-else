# Write a python program to check whether a character is uppercase or lowercase alphabet.
character = input("enter a character:")
if character >= "a" and character<= "z":
    print("Lowercase latter")
elif   character>= "A" and character <= "Z":
    print("Uppercase latter")
else :
    print("it is not an alphabet")
