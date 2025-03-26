from random import randint

if __name__ == '__main__':
    balance = randint(0, 100)
    price = 50
    print(f"余额：{balance}")
    if balance < price:
        print("余额不足,充值")
    else:
        balance = balance - price
        print(f"消费成功,余额:{balance}")
    print("欢迎下次光临")

    num1 = 2
    num2 = 3
    max_num = num1 if num1 > num2 else num2
    print("max_num=", max_num)
