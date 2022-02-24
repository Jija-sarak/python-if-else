# Write a python program to input angles of a triangle and check whether triangle is valid or not.
angle = int(input("enter a measurement of a angle"))
angle2 = int(input("enter a measurement of a angle"))
angle3 = int(input("enter a measurement of a angle"))
if angle + angle2 + angle3 == 180 :
    print("Valid")
else:
    print("invalid")