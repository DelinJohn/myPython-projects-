#  Write a program to add the values of two 2D arrays
class calculator():
         def addition(self,a,b):
             sum=a+b
             return sum
         def subtraction(self,a,b):
             difference=a-b
             return difference
         def multiplication(self,a,b):
             product=a*b
             return product
         def divition(self,a,b):
            if b!=0:
                quotient=a/b
                return quotient
            else:
                return print("invalid input")
        
a=["addition","subtraction","multiplication","division"]  
for i in range(4):  
    print(f"enter {i+1}for {a[i]} ")
size=int(input("enter your choice"))    
calc=calculator()  
if size==1:
     a=int(input("enter your first no"))
     b=int(input("enter your second no"))
     sum=calc.addition(a,b)
     print(sum)
elif size==2:
     a=int(input("enter your first no"))
     b=int(input("enter your second no"))
     sum=calc.subtraction(a,b)
     print(sum)
elif size==3:
     a=int(input("enter your first no"))
     b=int(input("enter your second no"))
     sum=calc.multiplication(a,b)
     print(sum)
elif size==4:
     a=int(input("enter your first no"))
     b=int(input("enter your second no"))
     sum=calc.divition(a,b)
     print(sum)
else:
    print("invaid entry")