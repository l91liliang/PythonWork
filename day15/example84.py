'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-10 22:18:36
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-10 22:59:17
FilePath: /PythonWork/day15/example84.py
Description: example84 - 继承

继承：对已有的类进行拓展创建出新的类，这个过程就叫继承。
     提供继承信息的类叫做父类（超类、基类），得到继承信息的类称为子类（派生类）。
继承是实现代码复用的一种手段。但是，千万不要滥用继承。

继承是一种is-a关系。
a student is a person.
a teacher is a person.
'''


class Person:
    """
    人类

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

    def play(self, game):
        """玩"""
        print(f'{self.name}正在玩{game}。')

    def watch(self):
        """看"""
        if self.age < 18:
            print(f'{self.name}未满18岁，不能观看。')
        else:
            print(f'{self.name}，大佐，请观看。')


class Student(Person):  # 继承，避免写了太多的重复语句
    """
    学生
    """

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}。')


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)  # super方法，等于把self.name = name、self.age = age调用过来了。
        self.title = title


def main():
    stu1 = Student('FMM', 28)
    print(stu1.age)
    stu1.study('love')
    stu1.eat()
    tea1 = Teacher('Larry', 28, 'engineer')
    print(tea1.title)


if __name__ == '__main__':
    main()
