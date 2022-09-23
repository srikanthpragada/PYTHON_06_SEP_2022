s = "10,20,50,50,ab,60,60"

total = 0
for v in s.split(","):
    if v.isdigit():
        total += int(v)

print(total)


