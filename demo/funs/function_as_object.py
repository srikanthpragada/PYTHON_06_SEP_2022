def fun():
    print("In fun()")


fun2 = fun

s = "abc"
print(type(s), type(fun))
fun()
fun2()
