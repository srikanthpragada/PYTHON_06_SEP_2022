data = [(1, 80), (2, 85), (1, 78), (4, 50), (2, 99), (2, 60)]

students = {}
for rollno, marks in data:
    l = students.get(rollno, [])
    l.append(marks)
    students[rollno] = l

print(students)
