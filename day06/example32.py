"""
example32 - 列表的相关操作

Author: larry
Date: 10/7/22

"""
# 生成列表有三种办法：

# 一、以下为字面量语法
list1 = ['apple', 'orange', 'pitaya', 'durian']  # 同一列表最好不要放不同类型的数据

# 二、以下为构造器语法：
list2 = list('abcdefg')  # 此列表中每个字符是一个元素。
print(list2)
items1 = list(range(1, 10))
print(items1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
items2 = list('hello')
print(items2)  # ['h', 'e', 'l', 'l', 'o']

# 三、以下为生成式语法（推导式语法）：
list3 = [i ** 2 for i in range(1, 10)]
print(list3)

# 获取列表元素的个数--->len()
print(len(list1))  # 4个

# 遍历列表中的元素
for i in range(len(list1)):
    print(list1[i])

print('---' * 50)

for x in list1:  # 只读
    print(x)

print('---' * 50)

for i, x in enumerate(list1):  # 枚举，既获取下标，又获取元素。推荐此种写法。
    print(i, x)

# 列表的运算
# 重复运算
list4 = [1, 10, 100] * 5
print(list4)

# 成员运算--->结果为True/False
print(10 in list4)  # 返回一个bool值True
print(5 in list4)  # 返回一个bool值False
print('pitaya' in list1)  # True
print('grape' in list1)  # False

# 索引和切片，非常重要！！！
# 正向索引：0～N-1
# 负向索引：-N～-1
print(list1[0], list1[-4], list1[-len(list1)])  # 输出的都是apple

# 切片
print(list2[0:5], list2[:5], list2[-7:-2], list2[:-2])  # 输出的都是['a', 'b', 'c', 'd', 'e']

# 合并运算
list5 = [1, 3, 5, 7]
list6 = [4, 4, 8]
temp = list5 + list6
print(temp)

# 比较（可比较两个列表是否相等 以及 对应索引位置上的元素的大小）实际工作中使用较少
list7 = list(range(1, 8, 2))
list8 = [1, 3, 5, 7, 9]
print(list5 == list7)  # 比较两个列表元素是否一一对应相等，返回一个bool值True
print(list7 == list8)  # 比较两个列表元素是否一一对应相等，返回一个bool值False
print(list7 < list8)  # 比较两个列表对应索引位置上的元素大小，返回一个bool值True
