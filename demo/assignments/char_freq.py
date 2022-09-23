s = "how do you do"

for c in sorted(set(s)):
    print(f"{c} - {s.count(c)}")