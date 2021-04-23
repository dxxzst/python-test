import turtle as t

"""
多行
注释
可以
不错
"""

# 单行注释
print('Hello World')

# t.setup(width=0.6, height=0.6)
# t.pensize(4)
# t.pencolor('red')
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.mainloop()

message = "hello world again"
print(message.islower())

firstName = "  ada   "
lastName = "   love "
fullName = f"{firstName.strip()} {lastName.strip()}"
print(fullName)

# t.color("red", "yellow")
# t.speed(10)
# t.begin_fill()
# for _ in range(50):
#     t.forward(200)
#     t.left(170)
# t.end_fill()
# t.mainloop()

testList = ["A", "B", "Hi", "B", "CDE"]
print(testList)
testList.append("DDD")
print(testList)
testList.pop()
print(testList)
testList.remove("B")
print(testList)
del testList[0]
print(testList)

print(sorted(testList))

testList.sort()
print(testList)
testList.reverse()
print(testList)
print(len(testList))

for item in testList:
    print(f"Hello this is {item.lower()}")

squares = [item ** item for item in range(1, 190)]
print(squares)

myTuple = ("Hell0", "World", 123)
print(myTuple)

tuple2 = tuple()
