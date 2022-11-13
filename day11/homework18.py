"""
homework18 - 双色球随机选号（实现机选N注）

红球01-33，选择不重复的6个球，按从小到大排列
蓝色球01-16，选择一个球，跟在红色球的后面


Author: larry
Date: 10/21/22

"""
from random import choice as choice
from random import sample as sample


def select_balls():
    """
    选择球

    :return: 返回选出的球红、蓝球组合列表
    """
    reds = [x for x in range(1, 34)]
    blues = [y for y in range(1, 17)]
    selected_red_nums = []
    # 此句可以简化：
    # for _ in range(6):
    #     red_num = choice(reds)
    #     selected_red_nums.append(red_num)
    #     reds.remove(red_num)
    selected_red_nums = sample(reds, 6)  # 此为不放回抽样
    selected_blue_num = choice(blues)
    select_nums = selected_red_nums
    select_nums.sort(key=int)
    select_nums.append(selected_blue_num)
    return select_nums


def print_balls(select_nums):
    """
    展示球

    :param select_nums: 选出的球红、蓝球组合列表
    """
    # print(select_nums)# 此句可以美化输出：
    for select_num in select_nums:
        print(f'{select_num:0>2d}', end=' ')  # 在个位数前加0


N = int(input('请输入你要买的注数：'))

for _ in range(N):
    print_balls(select_balls())
    print('')
