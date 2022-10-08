def numbers():
    for n in range(5):
        yield n


n = numbers()
print(type(n))
print(next(n))
print(next(n))
