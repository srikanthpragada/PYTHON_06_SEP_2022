class InvalidCourseError(Exception):
    def __init__(self, course):
        self.course = course

    def __str__(self):
        return f"Invalid course -> {self.course}"


class Student:
    # class attributes or static attributes
    courses = {'c': 5000, 'java': 10000, 'python': 12000}

    @staticmethod
    def gettotalfee(course):
        return Student.courses[course]

    def __init__(self, name, course='c', feepaid=0):
        # Object attributes
        if course not in Student.courses:
            raise InvalidCourseError(course)

        self.name = name
        self.course = course
        self.feepaid = feepaid


    def payment(self, amount):
        self.feepaid += amount

    def totalfee(self):
        return Student.courses[self.course]

    def dueamount(self):
        return self.totalfee() - self.feepaid


print(Student.gettotalfee('java'))

s1 = Student("Tom", "java")
s1.payment(5000)
s1.payment(3000)
s2 = Student("Bill")
s2.payment(5000)
print(s1.dueamount())
print(s2.dueamount())

s3 = Student("Jack", ".Net")

