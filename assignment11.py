# Write a program to identify whether a string is a palindrome or not without using reverse(), slicing
name=input ("enter the name:")     
n=len(name)
for i in range(n//2):
        if name[i]==name[n-i-1]:
            print("entered string is a palinadrome")
            break
        else:
            print("it is not")     
            break    
