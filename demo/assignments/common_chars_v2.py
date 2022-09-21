s1 = "java"
s2 = "kava"

common = []
for c in s1:
    if c in s2 and c not in common:
        print(c)
        common.append(c)

