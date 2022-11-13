'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-06 13:38:57
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-06 15:29:28
FilePath: /PythonWork/day14/example80.py
Description: example80 - 
'''
from example79 import Card,Suite
import random


class Poker:
    """扑克"""

    def __init__(self) -> None:
        self.cards = [Card(suite, face)
                      for suite in Suite for face in range(1, 14) ]  # 生成式语法，等效替代下列循环。
        # for suite in 'SHCD':
        #     for face in range(1, 14):
        #         card = Card(suite, face)
        #         self.cards.append(card)
        self.counter = 0

    def shuffle(self):
        """洗牌"""
        self.counter = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.counter]
        self.counter += 1
        return card

    def has_more(self) -> bool:
        """是否还有牌"""
        return self.counter < len(self.cards)


def main():
    poker = Poker()
    poker.shuffle()
    while poker.has_more():
        print(poker.deal(), end=' ')
    # print(poker.cards)


if __name__ == '__main__':
    main()
