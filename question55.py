# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the 
# given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
string = input("enter a string")
if len(string)>=3 and string[-3:]!="ing":
    print(string+"ing")
elif string[-3:]=="ing":
    print(string[:-3]+"ly")
else:
    print(string)