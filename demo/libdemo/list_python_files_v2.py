import os

gen = os.walk(r"d:\classroom\sep6\demo")
for (dname, dirs, files) in gen:
    count = 0
    print(f'Directory : {dname}')
    print("-" * 60)
    for f in files:
        if f.endswith(".py"):
            print(f)
            count += 1

    print(f"Count = {count}")
