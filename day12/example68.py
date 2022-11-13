"""
example68 - 位置参数、关键字参数

Author: larry
Date: 10/29/22

"""
import utils

# 调用函数时，如果希望函数的调用者'必须'以`参数名=参数值`的方式传参，可以用命名关键字参数（keyword-only argument）取代位置参数。
# 所谓命名关键字参数,是在函数的参数列表中，写在*之后的参数，代码如下所示。写在*值钱的参数称为位置参数，调用函数传递参数时，只需要对号入座。
print(utils.get_suffix('hello.py'))
print(utils.get_suffix('hello.py', has_dot=True))
print(utils.get_suffix('hello.py.txt'))
print(utils.get_suffix('hello.py.txt', has_dot=True))
print(utils.get_suffix('hello.'))
print(utils.get_suffix('.hello'))
