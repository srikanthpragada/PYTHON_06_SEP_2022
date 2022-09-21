s = "this is to test how it works"

lw = ""
for w in s.split():
    if len(w) >= len(lw):
        lw = w

print(lw)
