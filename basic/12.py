def fibonacci_1(count):
    n, a, b = 0, 0, 1
    while n < count:
        print(b, end=' ')
        a, b = b, a + b
        n = n + 1
    return "finish"


def fibonacci_2(count):
    n, a, b = 0, 0, 1
    while n < count:
        yield b
        a, b = b, a + b
        n = n + 1
    return "finish"


def my_yield():
    print("第1次运行")
    yield 1
    print("第2次运行")
    yield 2
    print("第3次运行")
    yield 3
    return print("is ok")


if __name__ == "__main__":
    # fibonacci_1(10)
    func = fibonacci_2(10)
    for num in func:
        print(num, end=' ')

    print("\n")

    temp = my_yield()
    ret_yield = next(temp)
    print(ret_yield)
    ret_yield = next(temp)
    print(ret_yield)
    ret_yield = next(temp)
    print(ret_yield)
