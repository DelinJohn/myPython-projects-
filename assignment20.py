# Write a program to include all the functionalities of a calculator using ABSTRACT class and abstract method. All the methods (add, sub, mul, div) should be inside of abstract class. Abstract method definition should be in another class
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