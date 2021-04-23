import time
from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    # f = open('test.txt', 'r', encoding='utf-8')
    # print(f.read())
    # f.close()

    # try:
    #     with open('test.txt', 'r', encoding='utf-8') as f:
    #         print(f.read())
    # except FileNotFoundError:
    #     print('无法打开指定的文件!')
    # except LookupError:
    #     print('指定了未知的编码!')
    # except UnicodeDecodeError:
    #     print('读取文件时解码错误!')

    # with open('test.txt', 'r', encoding='utf-8') as f:
    #     print(f.read())
    # print('\n')
    #
    # # 通过for-in循环逐行读取
    # with open('test.txt', mode='r', encoding='utf-8') as f:
    #     for line in f:
    #         print(line, end='')
    #         time.sleep(0.5)
    # print('\n')
    #
    # # 读取文件按行读取到列表中
    # with open('test.txt', encoding='utf-8') as f:
    #     lines = f.readlines()
    # print(lines)

    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


if __name__ == '__main__':
    # from random import randint
    #
    # for _ in range(0, 100):
    #     num = randint(0, 6)
    #     print(num)

    print(tuple({1, 2, 3, 6, 3}))

    main()
