if __name__ == '__main__':
    dict1 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
    keys = dict1.keys()
    for key in keys:
        print(key)
    items = dict1.items()
    for item in items:
        print(item, type(item))
    del dict1["key1"]
    print(dict1)
    # 整个清空
    # dict1.clear()
    # print(dict1)
    # 删除
    # print(dict1.pop("key2"))
    # print(dict1)
    # 取出最后的元素
    popitem = dict1.popitem()
    print(popitem, dict1)

    dict2 = dict()
    print(dict2, type(dict2))
    dict2.setdefault("zha")
    print(dict2)
    dict2.update(dict1)
    print(dict2)

