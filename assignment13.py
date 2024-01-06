# Grades are computed using a weighted average. Suppose that the written test counts 70%,  lab exams 20% and assignments 10%.
marks=[int(input("enter your theory marks")),int(input("enter youe practical marks")),int(input("enter your assignment mark"))]
weightage=[.7,.2,.1]
print(f"theory marks{marks[0]}, practical marks{marks[1]}, assignment marks{marks[2]}")
grade_percentage=sum(marks[i]*weightage[i] for i in range(3))
print(grade_percentage)