"""
example28 - 容器型数据类型

～ 列表（list）：比较常用--->一个变量保存多个数值（用一个变量可以保存多个数据）
～ 元组（tuple）
～ 集合（set）
～ 字典（dict）



Author: larry
Date: 10/5/22

"""
nums = [10, 100, 1000]  # 列表
print(nums)
print(type(nums))
rules = ['热爱祖国，热爱人民',
         '尊敬师长，团结同学',
         '好好学习，天天向上']
print(rules)

nums.append(10000)  # 代表在最后插入元素。
nums.insert(0, 1)  # 代表在0号元素前，插入一个"1"元素。
print(nums)

rules.pop()  # 默认干掉最后一个元素
print(rules)

