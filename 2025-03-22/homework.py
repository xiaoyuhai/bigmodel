def q1(x):
    # while True:
    if x > 0:
        print("正数")
    elif x == 0:
        print("0")
    else:
        print("负数")


def q2():
    for i in range(1, 11):
        print(i)
    # for i in 1, 10:
    #     print(i)


def q3():
    for i in range(1, 11):
        if i % 2 == 0:
            print("i=", i, "偶数")
        else:
            print("i=", i, "奇数")


def q4():
    i = 0
    sum = 0
    while i <= 100:
        sum += i
        i = i + 1
    print("1到100的和=", sum)


def q4sim():
    sum = 100 * (100 + 1) / 2
    print(sum)


if __name__ == '__main__':
    q1(-1)
    q2()
    q3()
    q4()
    q4sim()
