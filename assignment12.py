# Write a program to add to two dimensional arrays, understand the memory management of list
print("first matrix")
row=int(input("enter the row"))
column=int(input("enter the coloumn:"))
first_matrix= [[int(input(f"Enter the value for row {i+1} column {j+1}: ")) for j in range(column)] for i in range(row)]
print("second matrix")
second_matrix= [[int(input(f"Enter the value for row {j+1} column {i+1}: ")) for j in range(column)] for i in range(row)]
print("first matrix")
for r in  first_matrix:
    print(r)
print("second matrix")
for r in  second_matrix:
    print(r)
    
print("total matrix")    
total_matrix=[[first_matrix[i][j] + second_matrix[i][j] for j in range(column)] for i in range(row)]

for r in total_matrix:
    print(r)