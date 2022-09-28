def fun(p):
    print(id(p))
    p = 0


a = 100
print(id(a))
fun(a)
print(a)  # ?


def prepend(lst, value):
    lst.insert(0, value)


l = [1, 2]
prepend(l, 10)
print(l)
