"""
发礼物游戏
1、礼物标志
2、发礼物的方法
3、展示礼物的方法
4、运行入口
"""

have_gift = False


def send():
    global have_gift
    have_gift = True
    print('发礼物啦')


def show():
    if have_gift == True:
        print("收到礼物啦")
    else:
        print("没有收到礼物")


if __name__ == '__main__':
    send()
    show()
