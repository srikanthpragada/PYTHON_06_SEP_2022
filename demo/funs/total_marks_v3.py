data = "60:88:45::65:98"

marks  = []
for m in data.split(":"):
    if m.isdigit():
        marks.append(int(m))

print(sum(marks))
