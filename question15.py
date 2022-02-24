# Write a python program to input all sides of a triangle and check whether the triangle is valid or not.
side_a = int(input("enter a number:"))
side_b = int(input("enter a number:"))
side_c = int(input("enter a number:"))
if side_a+side_b>=side_c and side_c+side_b>=side_a and side_c+side_a >=side_b:
    print("valid triangle")
else:
    print("invalid triangle")