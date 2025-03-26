if __name__ == '__main__':
    rabbit = 2
    week = 1
    while week < 10:
        rabbit = rabbit + rabbit * 2
        week += 1
        print(f"第{week}周,有{rabbit}只兔子")
