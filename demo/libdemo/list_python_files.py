import os

gen = os.walk(r"d:\classroom\sep6\demo")
count = 0
for (dname, dirs, files) in gen:
    for f in files:
        if f.endswith(".py"):
            print(dname + "\\" + f)
            count += 1

print(f"Count = {count}")
