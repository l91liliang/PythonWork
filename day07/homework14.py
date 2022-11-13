"""
homework14 - 用一个列表保存54张扑克牌，先洗牌，
再按斗地主的发牌方式把牌发给三个玩家，多的3张牌给第一个玩家（地主），
最后把每个玩家手上的牌显示出来。


Author: larry
Date: 10/9/22



"""
import random

decors = ["♥", "♠", "♦", "♣"]
card_classes = [str(i) for i in range(2, 11)] + ["A", "J", "Q", "K"]
cards = [a + b for a in decors for b in card_classes] + ["KING", "QUEEN"]
random.shuffle(cards)
# user1 = []
# user2 = []
# user3 = []  # 这么写写的会很臃肿，所以需要写嵌套列表。
users = [[] for _ in range(3)]  # 嵌套列表，列表中的元素又是列表。
for _ in range(17):
    for user in users:
        user.append(cards.pop())
users[0].extend(cards)
for user in users:
    user.sort(key=lambda x: x[1:])
    for card in user:
        print(card, end=' ')
    print()

# user1.sort(key=lambda x: x[1:])
# user2.sort(key=lambda x: x[1:])
# user3.sort(key=lambda x: x[1:])
# print(f"user1的牌：{user1}")
# print(f"user2的牌：{user2}")
# print(f"user3的牌：{user3}")
