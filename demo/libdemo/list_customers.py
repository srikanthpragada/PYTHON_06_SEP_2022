import re

f = open("customers.txt", "rt")
customers = []
for line in f.readlines():
    # look for name
    m = re.search('[A-Za-z ]+', line)
    if m is None:
        continue

    name = m.group().strip()

    # look for mobile
    m = re.search(r'\d+', line)
    if m is None:
        continue

    mobile = m.group()

    customers.append((name, mobile))

f.close()

for name, mobile in sorted(customers):
    print(f"{name:20} {mobile}")
