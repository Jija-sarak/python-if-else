# Write a python program to calculate profit or loss.
cost = int(input("enter a amount:"))
selling_price = int(input("enter a amount"))
if cost < selling_price:
    print("profit =",selling_price - cost)
else:
    print("loss =",cost-selling_price)