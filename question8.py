# Write a python program to input any alphabet and check whether it is vowel or consonant.
latter = input("enter a alphabet:")
if latter == "a" and "i" and "o" and "u" and "e":
    print("it is a vowel")
elif latter == "A" and "I" and "O" and "U" and "E": 
        print("it is a vowel")
elif latter >= "a" and latter<="z" or latter >="A" and latter<="Z":
    print("it is a consonant")
else :
    print("neither vowel nor consonant")