# Write a program to create a copy of array and add an element to copied array . show both arrays.
size_array=int(input("enter the array limit"))
array1=[input("enter array elements")for elements in range(0,size_array)]
array2=array1.copy()

array2.append(input("enter the new element"))
print(f"orgianl array{array1}")
print(f"modified array{array2}")