#   Write a program to accept an array and display it on the console using functions
# Program should contain 3 functions including main() function

def get_array():
    n=int(input("enter the size of the array"))
    array=[int(input (f"enter the values of array element {i} "))for i in range(n)]
    return array
def display_array(arr):
    print(arr)

array_values=get_array()
display_array(array_values)
    
   
         
    