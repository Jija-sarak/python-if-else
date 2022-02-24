# A student will not be allowed to sit in an exam if his/her attendance is less than 75%.
# Take following input from the user. Number of classes held. Number of classes attended. 
# And print, percentage of class attended. Is the student is allowed to sit in the exam or not.
held_classes = int(input("enter the held classes:"))
attended_classes = int(input("enter the attedence"))
percentage = attended_classes/held_classes*100
if percentage >75:
    print(percentage,"A student is allowed to sit in the exam")
else:
    print(percentage,"A student is not allowed to sit in the exam")