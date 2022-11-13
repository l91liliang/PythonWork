'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-05 11:15:42
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-05 11:34:32
FilePath: /PythonWork/day14/example76.py
Description: example76- 用面向对象编程思想解决现实问题
'''
from math import pi as pi


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def perimeter(self):
        """圆的周长"""
        return 2*pi*self.radius

    def area(self):
        """圆的半径"""
        return pi*self.radius**2


if __name__ == '__main__':
    r = float(input('请输入游泳池（小圆）的半径:'))
    circle1 = Circle(r)
    circle2 = Circle(r+3)

    fence_price = circle2.perimeter()*38.5
    aisle_price = (circle2.area()-circle1.area())*58.5
    money = fence_price+aisle_price
    print(f'半径为{r}的游泳池，围墙造价为{fence_price:.2f}元，过道造价为{aisle_price:.2f}元，总造价为{money:.2f}元。')
