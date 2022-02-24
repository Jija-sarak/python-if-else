# Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java
string = input("enter a string:")
if string[-4:]=="Java" or string[-4:]=="Ruby" or string[-4:]=="HTML" or string[-4:]=="Rust" or string[-4:]=="Dart":
    print(string[-4:])
elif string[-6:]=="Python" or string[-6:]=="Kotlin" or string[-6:]=="MATLAB" or string[-6:]=="golang":
    print(string[-6:])
elif string[-10:]=="JavaScript":
    print(string[-10:])
elif string[-3:]=="PHP" or string[-3:]=="C++" or string[-3:]=="SQL" or string[-3:]=="Ada":
    print(string[-3:])
elif string[-2:]=="C#" :
    print(string[-2:])
elif string[-1:]=="C":
    print(string[-1:])
else:
    print("language is not found")
