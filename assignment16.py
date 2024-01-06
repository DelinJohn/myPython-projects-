# Write a program to print “HELLO WORLD “using function without using print inside of function. (“HELLO WORLD “must be inside Decorator function) 
def hello_wrapper(func):
    def sub_wrap():
        func()
    return sub_wrap
@hello_wrapper
def hello_world():
    print("hello world")
    
hello_world()
