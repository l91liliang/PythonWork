"""
example49 - 字符串的拆分和合并

Author: larry
Date: 10/15/22

"""
# 拆分--->把字符串进行拆分变成列表。
content = 'You go your way, I will go mine.'
content2 = content.replace(',', '').replace('.', '')
words = content2.split()  # 拆分，默认是以空格来拆分。
for word in words:
    print(word)

words = content2.split(' ', maxsplit=3)  # 拆分，可以用maxsplit方法限制拆分次数
for word in words:
    print(word)

content3 = content.split(',')
for x in content3:
    print(x)

# 合并、连接操作--->把列表元素进行合并，变成一个完整的元素。
contents = [
    '不要核酸要吃饭，不要封锁要自由',
    '不要谎言要尊严，不要文革要改革',
    '不要领袖要选票，不做奴才做公民',
    '罢课罢工罢免独裁国贼习近平'
]
print(contents)
print('~'.join(contents))  # 将列表中的元素用指定的字符串连接
