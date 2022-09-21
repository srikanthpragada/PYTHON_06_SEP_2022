l1 = [10, 20, 40, 50, 60]
l2 = [1, 2, 3, 4]

for v1, v2 in zip(l1, l2, strict=True):
    print(v1, v2)
