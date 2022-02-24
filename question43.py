# Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly
# If age does not fall in any range then display the following message: “Enter appropriate age”
# Age
# Sex
# Wage/day
# >=18 and <30
# M
# 700
# F
# 750
# >=30 and <=40
# M
# 800
# F
# 850
age = int(input("enter your age:"))
sex  = input("enter M or F:")
days = int(input("enter working days:"))
if age>=18 and age<30:
    if sex == "M":
        print("wages =",700*days)
    elif sex =="F":
        print("wages =",750*days)
    else:
        print("check your inputs")
elif age>=30 and age <=40:
    if sex == "M":
        print("wages =",800*days)
    elif sex =="F":
        print("wages =",850*days)
    else:
        print("check your inputs")
else:
    print("Enter appropriate age ")