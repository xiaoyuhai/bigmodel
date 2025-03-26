if __name__ == '__main__':
    list1 = [100, 200, 300, 150, 400, 500]
    print(list1[1])
    # 从后往前找
    print(list1[-1])
    # 下角标越界
    # print(list1[-6])
    # ;从开始到结束
    list2 = list1[:]
    print(list1, list2, "id=list1", id(list1), "id=list2", id(list2))

    list_ = list1[2:]
    print(list_)
    list3 = list1[:2]
    print(list3)
    # 步长是正数，正序递增
    print(type(range(0, 10, 1)))
    # for i in range(0, 10, 1):
    #     print(i)
    # for i in range(10, 1, -1):
    #     print(i)

    print(list1[0:3:-1])
    print(list1[3:0:1])

    for item in list1:
        print(item)

    # 打印效果
    for i, item in enumerate(list1):
        print("i=", i, "list1 item", item)
    # 删除列表元素
    del list1[2]
    print(list1)

    list1.remove(100)
    print(list1)

    # 删除元素
    print(list1.pop(1))
    print(list1)

    list3 = [1, 2, 3, [1, 5, 7]]
    print(list3[3])

    list4 = [i * 2 for i in range(5)]
    print(list4)

    list5 = [i * 2 for i in range(10) if i % 2 == 0]
    print(list5)

    list3 = ["a", "b", "c"]
    list4 = [j + i for i in list3 for j in list3]
    print(list4)

    # zip拉链函数
    z = zip([1, 2, 3], ["a", "b", "c"])

    print(type(z))
    for i in z:
        print(i)

    list6 = [1, 2, 3]
    list7 = ["a", "b"]
    print(list6.extend(list7))
