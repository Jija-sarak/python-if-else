# Write a program to accept the cost price of a bike and display the road tax to be paid according 
# to the following criteria : 
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                          10%
#         <= 50000                                                  5%
price = int(input("enter a amount:"))
if price<=50000:
    print("Tax =",price*5/100)
elif price >50000 and price<=100000:
    print("Tax =",price*10/100)
else:
    print("Tax =",price*15/100)