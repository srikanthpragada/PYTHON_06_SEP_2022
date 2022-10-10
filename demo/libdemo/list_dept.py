f = open("employees.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    salaries = [int(v) for v in parts[1:] if v.isdigit()]
    total = sum(salaries)
    print(f"{name:20}  {total:8} {total//len(salaries):8}")

f.close()


