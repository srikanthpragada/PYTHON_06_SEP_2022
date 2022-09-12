n = 127
prime = True
for i in range(2, n//2 +1):
    if n % i == 0:
        print("Not prime")
        prime = False
        break

if prime:
    print("Prime")