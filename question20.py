# Write a python program to input electricity unit charges and calculate total electricity bill according
# to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
E = int(input("enter units :"))
if E <=50 and E != 0 :
    K=E*0.50
    print(K+(K*20/100))
elif  E<=150 and E!=0 :
    E= E - 50 
    S=(E*0.75)+(50*0.50)
    print(S+(S*20/100))
elif E<=250 and E!=0:
    E -= 150
    J = E*1.20 +(100*0.75)+(50*0.50)
    print(J+(J*20/100))
elif E>250 and E!=0:
    E-=250
    A=(E*1.50+(100*1.20)+(100*0.75)+(50*0.50))
    print(A+(A*20/100))
else:
    print("No Charges")