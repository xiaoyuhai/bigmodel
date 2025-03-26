from random import randint

if __name__ == '__main__':
    balance = randint(0, 100)
    price = 50
    print(f"余额：{balance}")
    if balance < price:
        print("余额不足")
    print("欢迎下次光临")

    var = 100
    if var == 100: print("变量var的值为100")

