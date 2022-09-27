def extract_upper(s):
    r = ""
    for c in s:
        if c.isupper():
            r = r + c

    return r


names = ["Java", "PYThon", "C#"]

for v in map(extract_upper, names):
    print(v)
