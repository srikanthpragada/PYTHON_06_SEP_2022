data = [(1, 80), (2, 85), (1, 78), (4, 50), (2, 99), (2, 60)]

students = {}
for rollno, marks in data:
      students[rollno] = students.get(rollno,0) + marks

print(students)



