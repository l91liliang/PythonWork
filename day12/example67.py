"""
example67 - 解决命名冲突的两种方式
方式一：导入的时候采用别名
方法二：使用完全限定名（qualified name）--->包名.模块名.函数名

Author: larry
Date: 10/29/22

"""
from utils.bar import say_hello as s1
from utils.foo import say_hello as s2
import utils.bar
import utils.foo

s1()
s2()

utils.bar.say_hello()
utils.foo.say_hello()