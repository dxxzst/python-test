# def factorial(num):
#     result = 1
#     for x in range(1, num + 1):
#         result *= x
#     return result
#
#
# m = int(input('m = '))
# n = int(input('n = '))
# # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
# print(factorial(m) // factorial(n) // factorial(m - n))


# def add(a=1, b=2, c=3):
#     return a + b + c
#
#
# print(add())
# print(add(2, 3, 4))
# print(add(c=2, a=3, b=4))


# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total


def test_name(*args):
    print(args)


if __name__ == '__main__':
    # print(add())
    # print(add(1, 2))
    # print(add(1, 2, 3, 4, 5))
    test_name(11, 2323, "try", {"key": 2})
