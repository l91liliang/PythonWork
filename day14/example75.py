'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-05 11:01:25
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-10 22:13:01
FilePath: /PythonWork/day14/example75.py
Description: example75 - 创建对象/给对象发消息
'''
from example74 import Student

# 第二步：创建对象--->构造器语法--->类名(...,...)
stu1 = Student('FMM', 28)
stu2 = Student('Larry', 28)

# 第三步: 给对象发消息（调用对象的方法）
stu1.eat()
stu1.study('吃屎')
stu1.watch()
stu1.watch()
