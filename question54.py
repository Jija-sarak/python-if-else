# Write a Python program to calculate the length of a string.


a  = int(input("enter a number :"))
b = int(input("enter a number :"))
c = int(input("enter a number :"))
# if a > c and a < b or a > b and a < c :
#     print(a)
# elif c>a and c <b or c>b and c <a:
#     print(c)
# else:
#     print(b)
if a > c :
   if a < b :
       print(a)
if a > b :
    if a < c :
        print(a)
if c > a :
    if c < b :
        print(c)
if c>b :
    if c < a :
        print(c)
if  b < a:
    if b >c:
        print(b)
if b > a :
    if b < c :
        print(b)


    
