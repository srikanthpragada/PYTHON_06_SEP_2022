n = 127
for i in range(2, n//2 +1):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")