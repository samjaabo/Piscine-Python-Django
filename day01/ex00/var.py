def my_var():
    a = 42              # int
    b = "42"            # str
    c = 'quarante-deux' # str
    d = 42.0            # float
    e = True            # str
    f = [42,]           # list
    g = {42: 42,}       # dict
    h = (42,)           # tuple
    i = {42,}           # set
    print(a, 'has a type', type(a))
    print(b, 'has a type', type(b))
    print(c, 'has a type', type(c))
    print(d, 'has a type', type(d))
    print(e, 'has a type', type(e))
    print(f, 'has a type', type(f))
    print(g, 'has a type', type(g))
    print(h, 'has a type', type(h))
    print(i, 'has a type', type(i))

if __name__ == '__main__':
    my_var()