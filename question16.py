# Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=int(input("enter the number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isosceles")
else:
    print("scelene")        