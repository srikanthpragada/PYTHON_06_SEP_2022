def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def showall(*args, **kwargs):
    pass


show(a=10, x=20, name="Abc")
show(x=10, y=20, radius=30)
showall(10, 20, 30, name='Python', version=3.10)
