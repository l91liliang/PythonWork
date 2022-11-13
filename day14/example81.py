'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-06 15:30:45
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-10 21:25:18
FilePath: /PythonWork/day14/example81.py
Description: example81 - 玩家
'''
from example80 import Poker


class Player:

    """玩家"""

    def __init__(self, nickname) -> None:
        self.nickname = nickname
        self.cards = []

    def get_one_card(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()

    def show(self):
        """显示玩家手上的牌"""
        result = self.nickname+':'+','.join('%s' % a for a in self.cards)
        return (result)


def main():
    poker = Poker()
    poker.shuffle()
    player1 = Player('FMM')
    player2 = Player('Larry')
    player3 = Player('aa')
    player4 = Player('bb')
    for _ in range(13):
        card = poker.deal()
        player1.get_one_card(card)
        card = poker.deal()
        player2.get_one_card(card)
        card = poker.deal()
        player3.get_one_card(card)
        card = poker.deal()
        player4.get_one_card(card)

    print(player1.show())
    print(player2.show())
    print(player3.show())
    print(player4.show())




if __name__ == '__main__':
    main()
