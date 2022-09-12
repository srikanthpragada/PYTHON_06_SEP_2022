
n1, n2 = 15, 45

smallest = n1 if n1 < n2 else n2

for i in range(2, smallest // 2 + 1):
    if n1 % i == 0 and n2 % i == 0:
        print(i)

