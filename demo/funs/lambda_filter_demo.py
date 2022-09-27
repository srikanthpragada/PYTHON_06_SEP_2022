l = [10, 11, 20, 44, 55, 60]

for n in filter(lambda v: v % 2 == 0, l):
    print(n)

names = ["Python", "java", "C++", "sql"]

for n in filter(lambda s: s[0].isupper(), names):
    print(n)
