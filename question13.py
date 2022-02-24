# Write a python program to count the total number of notes in a given amount.
amount = int(input("enter a amount:"))
if amount >=1:
    a  = amount//2000
    print("2000 =",a)
amount = amount % 2000
if amount< 2000:
    c = amount//500
    print("500 =",c)
amount= amount%500
if amount<500:
    d = amount//200
    print("200 =",d)
amount=amount%200
if amount<200:
    e = amount//100
    print("100 =",e)
amount=amount%100
if amount<100:
    f = amount//50
    print("50 =",f)
amount=amount%50
if amount<50:
    g = amount//20
    print("20 =",g)
amount=amount%20
if amount<20:
    h = amount//10
    print("10 =",h)
amount=amount%10
if amount<10:
    i = amount//5
    print("5 =",i)
amount=amount%5
if amount<5:
    j = amount//2
    amount=amount%2
    print("2 =",j)
    print("1 =",amount)
print("notes =",a+c+d+e+f+g+h+i+j+amount)

