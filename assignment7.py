# Write a program to print the multiplication table of given numbers. Using for and while

num=int(input("enter the number that you need multiplication table of"))
for i in range (1,11):
    ans=num*i
    print(f"{num}x{i}={ans}")
    
