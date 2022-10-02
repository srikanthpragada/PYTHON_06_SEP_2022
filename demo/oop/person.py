class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __gt__(self, other):
        return self.age > other.age


p1 = Person("Bill", 40)
p2 = Person("Bill", 40)
p3 = Person("Larry", 30)
print(p1 == p2)  # p1.__eq__(p2)
print(str(p1))  # p1.__str__()
#print(p1 > p3)

persons = [Person("A", 20), Person("B", 50), Person("C", 30)]
for p in sorted(persons):
    print(p)
