#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example73.py - 函数可以自己调用自己吗？？？
函数如果直接或间接的调用了自身，这种调用称为递归调用。
函数可以调别人，也可以调自己，但是一定要收敛。而且要尽快结束，不要无限制的调用。

如果一个函数（通常指递归调用的函数）不能够快速收敛，那么就很有可能产生下面的错误：
    - RecursionError: maximum recursion depth exceeded
最终导致程序的崩溃

递归函数的两个要点：
    1.递归公式（第n次跟第n-1次的关系）
    2.收敛条件（什么时候停止递归调用）

foo ---> fuck up
bar ---> beyond all recognition
@Time    :   2022/11/01 20:51:28
@Author  :   Larry 
@Version :   1.0
@Contact :   l91liliang@hotmail.com
@License :   
@Desc    :   None
'''


def foo():
    print('foo')


def bar():
    foo()
    print('bar')


def main():
    bar()
    print('Game over.')


if __name__ == '__main__':
    main()

# 利用递归算法写阶乘运算函数:


def fac(num):
    """
    求阶乘（递归写法）
    
    """
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


if __name__ == '__main__':
    for i in range(10):
        print(i, fac(i))
