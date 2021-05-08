import sys

print(sys.argv)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __str__(self):
        return "fib class"

    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):  # n是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # n是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            _list = []
            for x in range(stop):
                if x >= start:
                    _list.append(a)
                a, b = b, a + b
            return _list

    def __call__(self, *args, **kwargs):
        return self.__getitem__(100)


print(Fib())  # 输出自定义__str__

# f = Fib()
# print(f[0:35])
#
# for n in Fib():
#     print(n)

f1 = Fib()
print(f1())

print(callable(f1))  # 可调用对象
