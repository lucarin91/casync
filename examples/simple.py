from casync import af, Executor


def fun1():
    return 'hello'


def fun2():
    return 'world'


def concat(s1, s2):
    return s1 + ' ' + s2


def main():
    comp1 = af(fun1) & af(fun2)
    comp2 = af(fun1) | af(fun2)
    comp3 = comp1 >> af(concat)

    ex = Executor()
    res1 = ex(comp1)  # ('hello', 'world')
    res2 = ex(comp2)  # 'hello' or 'world'
    res3 = ex(comp3)  # 'hello world'

    print(res1, res2, res3)


if __name__ == '__main__':
    main()
