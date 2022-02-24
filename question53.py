# Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:
# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48                                                              
# 6 x 9 = 54                                                              
# 6 x 10 = 60
num = int(input("enter a number"))
if num>0:
    print(num,"*",1,"=",num*1)
    print(num,"*",2,"=",num*2)
    print(num,"*",3,"=",num*3)
    print(num,"*",4,"=",num*4)
    print(num,"*",5,"=",num*5)
    print(num,"*",6,"=",num*6)
    print(num,"*",7,"=",num*7)
    print(num,"*",8,"=",num*8)
    print(num,"*",9,"=",num*9)
    print(num,"*",10,"=",num*10)
else:
    print("enter aproprite number")