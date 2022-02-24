# Take the age of 3 people by user and determine oldest and youngest among them.
one = int(input("enter your age:"))
two = int(input("enter your age:"))
three = int(input("enter your age:"))
if one> two and one >three :
    print(one,"oldest")
if two > one and two > three:
    print(two,"oldest")
if three > one and three > two:
    print(three,"oldest")
if one<two and one<three:
    print(one,"youngest")
elif two < one and two < three:
    print(two,"youngest")
else:
    print(three,"youngest")