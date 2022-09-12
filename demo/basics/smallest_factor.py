# Smallest factor
n = 23

for i in range(2, n//2 + 1):
    if n % i == 0:
        print(i)
        break
else:
    print(n)

