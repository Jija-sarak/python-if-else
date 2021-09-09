# ATM code 
print("welcome to HDFC Bank")
card = (input("please insert your card"))
if card =="ATM card" or "Debit card":
    print("do not remove your card during the entire transaction")
    language = input("please Choose language :english or hindi")
    if language=="english":
       pin = int(input("enter your four digit number"))
       Balance = 100000
       if pin== 2304:
          print("1 = withdraw")
          print("2 = balance inquiry")
          print("3 = fast cash")
          transaction = int(input("please choose transaction"))
          account = input("please choose account: savings or current")
          if account=="currunt" or "savings":
              print("proceed transaction")
              if transaction==1 :
                 withdraw = int(input("please enter withdraw amount"))
                 if Balance>withdraw or Balance%withdraw==o:
                    new_balance = (Balance - withdraw)
                    print("collect your cash :rupees",withdraw)
                    print("remaning amount: rupees",new_balance)
                 else :
                    print("invalid cash")
              elif transaction==2:
                   print("your balance :rupees",Balance)
              elif transaction==3:
                   print("1 = 5000")
                   print("2 = 10000")
                   print("3 = 15000")
                   print("4 = 20000")
                   if Balance>5000:
                      fast_cash = int (input("enter fast cash amount"))
                      print("collect your cash :rupees",fast_cash)
                      print("remaining balance : rupees",Balance - fast_cash)
                   elif Balance>10000:
                      print("collect your cash:rupees",fast_cash)
                   elif Balance>15000:
                      print("collect your cash :rupees",fast_cash)
                   elif Balance>20000:
                      print("collect your cash: rupees",fast_cash)
                   else:
                       print("invalid amount")
                   print("transaction completed")
                   print("Thank you!")
       else:
           print("invalid pin")
    else:
         print("invalid pin")
else:
    print("try again!")
print("Thank you!")
            
