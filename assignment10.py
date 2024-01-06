#  Write a program to sort an array in descending order without sort() and sorted() Program should accept and array, sort the array values in descending order and display it
def sort_array(array):
    n=len(array)
    for i in range(n):
        max_indent=i
        for j in range(i+1,n):
            if array[j]>array[max_indent]:
                max_indent=j
        array[i],array[max_indent]=array[max_indent],array[i]
        
array=[20,10,30,25,5]                
sort_array(array)
print(array)
            
        
        
        

