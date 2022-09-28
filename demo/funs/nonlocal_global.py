def f1():
    a = 10

    def f2():
        nonlocal a
        a = 20

    f2()
    print(a)


f1()
