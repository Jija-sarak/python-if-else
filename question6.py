# Write a python program to check whether a year is leap year or not.
# 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056,
#  2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096.
year = int(input("enter a year"))
if year % 4 == 0 :
    print("year is leap year")
else:
    print("year is not leap year")

