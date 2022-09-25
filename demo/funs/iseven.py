def iseven(n: int) -> bool:
    return n % 2 == 0


def count_upper(s: str) -> int:
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def isprime(n: int) -> bool:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


print(iseven(10), iseven(11))
print(count_upper('AbcXyz'))
