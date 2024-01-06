# Write a function to calculate the sum of all numbers passed as its arguments. Your function should be called sum_numbers and should define a single variable       
# argument (i.e. a star argument) that will get the values to sum.
def calculate_sum(args):
    print(args)
    return sum(args)


numbers=input("enter the numbers with a space ")
list_numbers=[float(i )for i in numbers.split()]

result=calculate_sum(list_numbers)
print(result)
list1=[1,2,3,4,5,6,7]

total=sum(list1)
print(total)
