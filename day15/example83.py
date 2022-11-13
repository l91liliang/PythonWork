'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-10 21:55:09
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-10 22:15:33
FilePath: /PythonWork/day15/example83.py
Description: example83 - 避免在引用类的过程中，给类添加属性的行为。

Python中的继承允许多重继承，一个类可以有一个或多个父类。
如果不是必须使用多重继承的场景下，请尽量使用单一继承。
'''


class Student:  # 驼峰命名法
    """
    学生
    """
    __slots__ = (
        'name', 'age')  # 魔法方法，禁止在引用类的时候，添加另外的属性，如：本类的属性只能有'name'和'age，其他的都不能有。
    # 数据抽象

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 行为抽象
    def eat(self):
        """吃饭"""
        print(f'{self.name}，年龄{self.age}正在吃饭。')

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}。')

    def play(self, game):
        """玩"""
        print(f'{self.name}正在玩{game}。')

    def watch(self):
        """看"""
        if self.age < 18:
            print(f'{self.name}未满18岁，不能观看。')
        else:
            print(f'{self.name}，大佐，请观看。')


def main():
    stu1 = Student('FMM', 28)
    stu1.gender = 'female'  # 会报错，不能新增该属性。
    print(stu1.name)
    print(stu1.gender)


if __name__ == '__main__':
    main()
