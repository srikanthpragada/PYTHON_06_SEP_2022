l1 = [10, 20, 40, 50, 60]
l2 = [1, 2, 3, 4]

for idx, v1 in enumerate(l1):
    if idx >= len(l2):
        v2 = 'None'
    else:
        v2 = l2[idx]

    print(v1, v2)
