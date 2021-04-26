my_list = [1, 4, 6]
it = iter(my_list)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("打印完毕")
        break

