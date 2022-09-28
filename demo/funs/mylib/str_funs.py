def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


def count_digit(st):
    count = 0
    for c in st:
        if c.isdigit():
            count += 1

    return count


def has_upper(st):
    for c in st:
        if c.isupper():
            return True

    return False
