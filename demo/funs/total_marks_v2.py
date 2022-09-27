data = "60:88:45::65:98"

parts = data.split(":")
#print(parts)
marks = [int(m) for m in parts if m.isdigit()]
#print(marks)
total = sum(marks)
print(total)
