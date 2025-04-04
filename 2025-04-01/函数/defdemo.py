def add(a, b):
    return a + b


"""
一个*号，底层是元祖，两个星号是字典
"""


def add1(a, *b):
    sum = a
    print(type(b))
    for x in b:
        sum += x
    return sum


def add2(a, **b):
    print(type(b))


def print1():
    print("&&&" * 100)


def func(age, name):
    print(f"姓名{name},年林：{age}")


def func1(name, age=20):
    print(f"姓名{name},年林：{age}")


if __name__ == '__main__':
    print(add(1, 2))
    print(add("a", "b"))
    # print(add1(1, 2, 3, 4, "hahah"))
    print(add2(1, **{"key1": "value1"}))
    print(print1())

    list = [1, 2, 3]
    print(list * 3)
    func(name="hahah", age=188)
    func1(name="test")
    # print(add2(1, *{"key1", "value1"}))
    # 但却无法忘记你的脸，有没有人从告诉你，我很爱你，有没有人在你日记里哭泣
