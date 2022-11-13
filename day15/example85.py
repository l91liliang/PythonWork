'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-10 22:59:27
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-11 21:36:17
FilePath: /PythonWork/day15/example85.py
Description: example85 - 两个类之间有哪些可能的关系？？？

继承是实现代码复用的一种手段，但是千万不要滥用继承。

~ is-a关系 ：继承 ---> class Student(Person)
~ has-a关系：关联 ---> 把一个类的对象作为另外一个类的对象的属性
    a person has an identity card.
    a car has an engine.
    - （普通）关联
    -  强关联：整体和部分的关联，聚合和合成
~ use-a关系：依赖 ---> 一个类的对象作为另外一个类的方法的参数或返回值
    a person uses a vehicle.
'''


class Vechicle:
    """交通工具"""
    pass


class Horse(Vechicle):
    """马"""
    pass


class Motobike(Vechicle):
    """摩托车"""

    def __init__(self) -> None:
        self.engine = Engine()


class Engine:
    """引擎"""
    pass


class Follower:
    """徒弟"""

    def __init__(self, name) -> None:
        self.name = name

    def do_work(self):
        pass


class MrTong:
    """唐僧"""

    def __init__(self) -> None:
        self.followers = [Follower('孙悟空'), Follower(
            '猪八戒'), Follower('沙和尚')]  # has-a关系

    def drive(self, vechicle):  # use-a关系
        """驾驶"""
        pass
