# A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000.
# Ask the user for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.
quantity = int(input("enter the quantity :"))
quantity = quantity*100
if quantity >1000:
    discount = quantity*10/100
    print("discount =",discount,"\nTotal cost =",quantity-discount)
else:
    print("Total cost =",quantity)