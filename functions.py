def myFunc(a, b):
    return a*b


print(myFunc(3, 4))


def outer(a, b):
    c = 2

    def inner():
        print(c * (a*b))

    inner()


outer(3, 4)
