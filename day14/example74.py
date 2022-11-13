'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-04 23:21:03
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-05 10:50:58
FilePath: /PythonWork/day14/example74.py
Description: example74 - 面向对象编程

之前写的都叫指令式编程 ---> 面向过程（函数）编程 ---> 程序很简单的话，没有问题。
编程范式（程序设计的方法论）
    - 面向对象编程
    - 函数式编程

对象（具体）：对象是可以接收消息的实体，面向对象编程就是给对象发消息，达到解决问题的目标。

对象= 数据+函数（方法）--->对象将数据和操作数据的函数从逻辑上变成了一个整体。

类（类型）（抽象）：将一大类对象共同的特征（静态特征和动态特征）抽取出来之后，得到的一个抽象概念。

简单的说，类是对象的蓝图（模版），有了类才能够创建出这种类型的对象。

面向对象编程：
    1.定义类（关键，麻烦）---> 类的命名使用驼峰命名法（每个单词首字母大写）
        - 数据抽象 ： 找到和对象相关的静态特征（属性）
        - 行为抽象 ： 找到和对象相关的动态特征（方法）
    2.澡对象
    3.发消息

'''

# 第一步：定义类


class Student:  # 驼峰命名法
    """
    学生
    """
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
