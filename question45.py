# Accept the number of days from the user and calculate the charge for library according to following :
# First five days : Rs 2/day.
# Six to ten days  : Rs 3/day.
# Ten to 15 days  : Rs 4/day
# After 15 days    : Rs 5/day
days = int(input("enter active days:"))
if days <=5:
    print("library chares =",days*2)
elif days >=6 and days <10:
    days= days - 5
    print("library chares =",days*3+(5*2))
elif days >=10 and days <=15:
    days -= 9
    print("library chares =",(days*4)+(5*2)+(4*3))
else:
    days -= 15
    print("library chares =",(days*5)+(5*2)+(4*3)+(6*4))
    