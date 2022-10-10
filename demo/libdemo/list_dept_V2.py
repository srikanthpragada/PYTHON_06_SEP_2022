f = open("employees.txt", "rt")

depts = []
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    salaries = [int(v) for v in parts[1:] if v.isdigit()]
    total = sum(salaries)
    depts.append((name, total, total // len(salaries)))

f.close()

for name, total, avg in sorted(depts):
    print(f"{name:20}  {total:8} {avg:8}")

