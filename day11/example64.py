"""
example64 - 全局变量和局部变量

    -全局变量（没有写在任何函数里面的变量）
    -局部变量（定义在函数内部的变量）

Python程序中搜索一个变量是按照LEGB顺序进行搜索的
Local（局部） ---> Embeded（嵌套作用域） ---> Global（全局作用域） --->built-in（内置作用域）
global ---> 声明使用全局变量或者将一个局部变量放到全局作用域
nonlocal ---> 声明使用嵌套作用域的变量（不使用局部变量）

Author: larry
Date: 10/22/22

"""
x = 100  # 全局变量


def foo():
    x = 200

    def bar():
        # x = 300
        print(x)

    bar()
    print(x)  # 输出300


foo()  # 输出200

print(x)  # 输出100
