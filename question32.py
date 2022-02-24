# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#         Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
unit = int(input("enter unit:"))
if unit<=100:
    print("no charge")
elif unit<=200:
    unit=unit-100
    print(unit*5)
elif unit>200:
    unit=unit-150
    print(unit*10)
else:
    print(" no")