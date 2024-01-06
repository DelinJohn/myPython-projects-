# Write a program to print the following pattern using for loop
# 7 8 9 10 
# 4 5 6
# 2 3
# 1

value=10
for i in range(4):
   
    for j in range(4-i):
        print(value ,end=' ')
        value-=1
       
    print()
