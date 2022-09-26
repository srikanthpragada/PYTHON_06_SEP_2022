def iseven(n: int) -> bool:
    return n % 2 == 0


def isodd(n: int) -> bool:
    return n % 2 == 1


l = [10, 11, 20, 44, 55, 60]

for n in filter(isodd, l):
    print(n)
