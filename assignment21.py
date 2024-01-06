# Write a program to build a home. The Home class should define all the attributes of each room in a home. From the Home class create two homes. FirstHome and SecondHome. First home should have an extra study room as a method. SecondHome should have the work_area as an extra method. should use the concept of inheritance.

class Home:
    def __init__(self):
        pass

    def room1(self):
        width = int(input("enter the width of room1 in meters:"))
        breadth = int(input("enter the breadth of room1 in meters:"))
        print(f"Area of room1:{ width * breadth}square meter")

    def kitchen(self):
        width = int(input("enter the width of kitchen in meters:"))
        breadth =int(input("enter the breadth of kitchen  in meters:"))
        print(f"Area of kitchen:{ width * breadth}square meter")

class FirstHome(Home):
    def study_room(self):
        width = int(input("enter the width of study room in meters:"))
        breadth =int(input("enter the breadth of study room in meters:"))
        print(f"Area of study room in FirstHome:{width * breadth }square meter")

class SecondHome(Home):
    def work_area(self):
        width = int(input("enter the width of work area in meters:"))
        breadth =int(input("enter the breadth of work area in meters:")) 
        print(f"Area of work area in SecondHome:{ width * breadth}square meter")


first_home = FirstHome()
second_home = SecondHome()

print("First House specsin meters:")
print()
first_home.room1()
print()
first_home.kitchen()
print()
first_home.study_room()
print()
print("Second House specsin meters:")
second_home.room1()
print()
second_home.kitchen()
print()
second_home.work_area()




