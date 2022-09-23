data = [(1, 80), (2, 85), (1, 78), (4, 50), (2, 99), (2, 60)]

students = {}
for rollno, marks in data:
    if rollno in students:
        students[rollno] = students[rollno] + marks
    else:  # new student
        students[rollno] = marks

print(students)



