# Study about functions 
# User defined
# Types of Arguments
# Lambda
#       Write a program using user defined functions and lambda functions

def add(a,b):
    sum=a+b
    return sum
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
result=add(num1,num2)
print(result)


product=lambda x,y:x*y


answer=product(num1,num2)
print(f"this is printed using lambda{answer}")