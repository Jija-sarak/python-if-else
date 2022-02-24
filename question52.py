# 41. Write a Python program to get next day of a given date.
# Expected Output:
# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24  
year = int(input("enter a year :"))
month = int(input("enter a month[1-12] :"))
day = int(input("enter a day[1-31]"))
if month == 2:
    if day>0 and day<29 and year%4==0:
        print(day+1,"-",month,"-",year)
    elif day>0 and day<28:
        print(day+1,"-",month,"-",year)
    else:
        print("enter the correct day")
elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if day>0 and day<31:
        print(day+1,"-",month,"-",year)
    else:
        print("enter the correct day")
elif month == 4 or 6 or 9 or 11:
    if day>0 and day<30:
        print(day+1,"-",month,"-",year)
    else:
        print("enter the correct day")
else:
    print("enter the correct month")

