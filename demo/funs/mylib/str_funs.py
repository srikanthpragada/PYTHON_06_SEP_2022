def count_upper(st):
    """
    Returns number of uppercase letters in the given string
    :param st: String to search
    :return: Count of uppercase letters
    """
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


# Testing
if __name__ == '__main__':
    print(count_digit('123abc'))
    print(has_upper('123abc'))
