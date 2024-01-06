#  Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
marks=float(input("enter the marks"))
if marks>100 or marks<0:
    print("invalid entry")
elif 100>=marks>=90:
    print("A")
elif 90>marks>=80:
    print("B")
elif 80>marks>=70:
    print("C")
elif 70>marks>=60:
    print("D")
elif 60>marks>=50:
    print("E")
elif 50>marks:
    print("failed")
            