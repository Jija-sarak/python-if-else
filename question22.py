# A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years.
# Ask users for their salary and year of service andprint the net bonus amount.
year = int(input("enter year of service:"))
salary = int(input("enter your salary:"))
if year >=5:
    Bonus  = salary*5/100
    print("bonus =",Bonus,"\nsalary =",salary+Bonus)
else:
    print("salary =", salary)
