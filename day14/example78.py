'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-05 17:47:42
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-05 21:09:51
FilePath: /PythonWork/day14/example78.py
Description: example78 - 定义描述三角形的类，提供计算周长和面积的方法。

我们在类中写的函数，通常称之为方法，它们基本上都是发给对象的消息。
但是，有的时候，我们的消息并不想发给对象，而是希望发给这个类（类也是一个对象）。
静态方法 - 发给类的消息 ---> @staticmethod--->装饰器
类方法 - 发给类的消息 ---> @classmethod --->装饰器 ---> 第一个参数是接收消息的类



'''
from math import sqrt as sqrt


class Triangle:

    # def __init__(self, a, b, c) -> None:
    #     if a+b > c and b+c > a and a+c > b:
    #         self.a = a
    #         self.b = b
    #         self.c = c
    #     else:
    #         # 引发异常写法。此种写法比较不规范。
    #         raise ValueError(f'{a:.2f}、{b:.2f}、{c:.2f}三条边无法构成三角形。')

    def __init__(self, a, b, c) -> None:
        if not Triangle.is_vaild(a, b, c):
            raise ValueError(f'{a:.2f}、{b:.2f}、{c:.2f}三条边无法构成三角形。')
        self.a = a
        self.b = b
        self.c = c

    # def judge(self):#此种写法相对比较好。
    #     """判断三条边是否能构成三角形。"""
    #     if self.a+self.b > self.c and self.b+self.c > self.a and self.a+self.c > self.b:
    #         pass
    #     else:
    #         return f"{self.a:.2f}、{self.b:.2f}、{self.c:.2f}三条边无法构成三角形。"

    @staticmethod  # 静态方法
    def is_vaild(a, b, c):
        return a+b > c and b+c > a and a+c > b

    def perimeter(self):
        """计算周长。"""
        return self.a+self.b+self.c

    def area(self):
        """计算面积，海伦公式"""
        p = self.perimeter()/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))


if __name__ == '__main__':
    try:
        a = float(input("请输入第一条边长度："))
        b = float(input("请输入第二条边长度："))
        c = float(input("请输入第三条边长度："))

        triangle1 = Triangle(a, b, c)
        # judge_triangle = triangle1.judge()
        # if judge_triangle == f"{a:.2f}、{b:.2f}、{c:.2f}三条边无法构成三角形。":
        #     print(judge_triangle)
        # else:
        print(
            f"{a:.2f}、{b:.2f}、{c:.2f}三条边构成的三角形，周长{triangle1.perimeter():.2f}，面积{triangle1.area():.2f}")
    except ValueError as err:
        print(err)
