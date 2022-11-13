'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-11 22:11:52
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-12 17:26:14
FilePath: /PythonWork/day15/example86.py
Description: example86 - 工资（月薪）结算系统

面向对象编程的四大支柱：
～ 抽象（abstraction）：提取共性（定义类就是一个抽象过程，需要做数据抽象和行为抽象）
～ 封装（encapsulation）：把数据和操作数据的函数从逻辑上组装成一个整体（对象）。
    --->隐藏实现细节，暴露简单的调用接口。
～ 继承（inheritance）：扩展已有的类创建新类，实现对已有类的代码复用。
～ 多态（polymorphic）：给不同的对象发出同样的信息，不同的对象执行了不同的行为。
    --->方法重写。


三类员工：
~ 部门经理：固定月薪，15000元
~ 程序员：计时结算月薪，每小时200元
~ 销售员：底薪+提成，底薪1800元，销售额5%提成

录入员工信息，自动结算月薪。

子类对于父类已有的方法，重新给出自己的实现版本，这个过程叫做方法重写（override）。

在重写方法的过程中，不同的子类可以对父类的同一个方法给出不同的实现版本，那么该方法在运行时就会表现出多态行为。

'''
from abc import abstractmethod


class Employee:

    def __init__(self, num, name) -> None:
        self.num = num
        self.name = name

    @abstractmethod  # 装饰器
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):  # 方法重写
        return 15000


class Programmer(Employee):

    def __init__(self, num, name) -> None:
        super().__init__(num, name)
        self.working_hour = 0

    def get_salary(self):  # 方法重写
        return 200*self.working_hour


class Salesman(Employee):
    def __init__(self, num, name) -> None:
        super().__init__(num, name)
        self.sales = 0

    def get_salary(self):  # 方法重写
        return 1800+self.sales*0.05


def main():
    emps = [Manager(1, '刘备'), Programmer(2, '诸葛亮'), Salesman(
        3, '关羽'), Salesman(4, '张飞'), Programmer(5, '马超')]

    for emp in emps:
        if type(emp) == Programmer:
            emp.working_hour = float(input(f'请输入{emp.name}的本月工作时长：'))
        elif type(emp) == Salesman:
            emp.sales = float(input(f'请输入{emp.name}的本月销售额：'))
        print(f'{emp.name}本月工资：{emp.get_salary()}元。')


if __name__ == '__main__':
    main()
