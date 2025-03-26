if __name__ == '__main__':
    for i in [2, 3, 4, 5, 6]:
        print(i)
    for i in "hello world":
        print(i)
    # range 生成序列从-开始，到n，不包括n，也可以设置步长
    for i in range(10):
        print(i)

    for i in range(-10, 10):
        print(i)

    for i in range(1, 10, 2):
        print("有步长的i", i)
    # 乘法口诀
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{i}*{j}={i * j}", end="\t")
        print()


