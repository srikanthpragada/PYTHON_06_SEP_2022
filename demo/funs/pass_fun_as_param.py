def mathop(a, b, operation):
    print(operation(a, b))


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


mathop(10, 20, add)
mathop(10, 20, mul)
#mathop(10,20, len)

