data = ["Abc,39393933", "Xyz,3903903903", "Bbc,393939222", "Pqr,39393933"]

persons = {}

for entry in data:
    name, mobile = entry.split(",")
    persons[name] = mobile

for name, mobile in sorted(persons.items()):
    print(f"{name:20} {mobile}")
