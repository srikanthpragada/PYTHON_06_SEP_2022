data = "60:88:45::65:98"

valid_marks = filter(str.isdigit, data.split(":"))
total = sum(map(int, valid_marks ))
print(total)
