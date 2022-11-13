"""
homework17 - CRAPS赌博游戏--->骰子游戏

玩家摇两颗骰子，如果第一次摇出了7点或11点，玩家胜；
如果摇出了2点、3点、12点，庄家胜；
如果摇出了其他的点数，游戏继续，玩家重新摇骰子；
如果玩家摇出了第一次摇的点数，玩家胜；如果玩家摇出了7点，庄家胜；
如果玩家摇出其他点数，游戏继续，玩家重新摇骰子，直到分出胜负。

游戏开始值钱，玩家有1000元的初始资金，玩家可以下注，赢了获得下注的金额，输了就扣除下注的金额。
游戏结束的条件是玩家把钱输光。

程序中加了函数，以便简化程序。

Author: larry
Date: 10/19/22

"""
from random import randint as rand


def roll_dice(num):
    """
    摇骰子

    :param num: 骰子的数量（对自变量进行说明）
    :return: 摇出的点数（对因变量进行说明）
    """

    total = 0
    for _ in range(num):
        total += rand(1, 6)
    return total


def win():
    """
    玩家获胜

    :return:
    """
    global money
    money += bet_money
    print(f'玩家胜，玩家现有余额{money}元。')


def lose():
    """
    庄家胜

    :return:
    """
    global money
    money -= bet_money
    print(f'庄家胜，玩家现有余额{money}元。')


money = 1000

while money > 0:
    print(f'你现在的总资产是{money}元。')
    bet_money = 0
    while bet_money <= 0 or bet_money > money:
        try:
            bet_money = int(input('请输入下注金额：'))
        except ValueError:
            print('输入错误。')
    first_point = roll_dice(2)
    print(f'本次你掷出的是{first_point}点。')
    if first_point in (7, 10):
        win()
    elif first_point in (2, 3, 12):
        lose()
    else:
        while True:
            curr_point = roll_dice(2)
            print(f'本次你掷出的是{curr_point}点。')
            if curr_point == first_point:
                win()
                break
            elif curr_point == 7:
                lose()
                break
            else:
                pass

if money <= 0:
    print('你破产了。')
