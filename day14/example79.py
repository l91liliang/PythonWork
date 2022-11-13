'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-06 10:22:21
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-10 21:39:33
FilePath: /PythonWork/day14/example79.py
Description: example79 - 扑克游戏，四个玩家参与，先洗牌，再把牌发到四个玩家的手上。
    -牌(Card)
        -属性：花色（suite）、点数（face）
        -行为：显示
    -扑克（Poker）
        -属性：保存牌的列表
        -行为：洗牌（shuffle）、发牌（deal）
    -玩家：
        -属性：名字（昵称）、保存玩家手牌的列表
        -行为：摸牌（get）、整理（arrange）

魔术方法（魔法方法） ---> 有特殊用途和意义的方法
    ~__init__ ---> 初始化方法，在调用构造器语法创建对象的时候会被自动调用
    ~__str__ ----> 获得对象的字符串表示，在调用print函数输出对象时会被自动调用
    ~__repr__ ---> 获得对象的字符串表示，把对象放到容器中，用print输出容器时会自动调用
        ---> representation

枚举类型：如果一个变量的取值只有有限个选项，可以考虑使用枚举类型。
        Python中没有定义枚举类型的语法，但是可以通过继承Enum类来实现枚举类型。
        结论1：枚举类型是定义符号常量的最佳选择。
        结论2:符号常量（有意义的名字）总是优于字面常量。
'''
from enum import Enum


class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = 0, 1, 2, 3


class Card:
    """牌"""

    def __init__(self, suite: Suite, face: int) -> None:
        self.suite = suite
        self.face = face

    def __repr__(self) -> str:
        return self.show()

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

    def show(self):
        """显示牌"""

        suites = ['♠️',  '♥️',  '♣️',  '♦️']
        faces = ['', 'A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'


def main():
    card1 = Card(Suite.HEART, 1)
    card2 = Card(Suite.SPADE, 13)
    print(card1, card2)
    print(card1 is card2)
    card3 = Card(Suite.DIAMOND, 9)
    card4 = Card(Suite.CLUB, 11)
    print(card3.show(), card4.show())
    card1 = card2
    print(card1, card2, card3)
    # 身份运算符
    print(card1 is card2)
    print(card1 is card3)
    cards = [card1, card2, card3, card4]
    print(cards)


if __name__ == '__main__':
    main()
