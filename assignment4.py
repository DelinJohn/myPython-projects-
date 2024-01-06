# Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).

marks=float(input("enter the marks"))
if marks>100 or marks<0:
    print("invalid entry")   
elif marks>=50:
    print("passed")
elif marks<50:
    print("failed")    
 