"""
example47 - 字符串的操作

Author: larry
Date: 10/15/22

"""
a = 'hello,world'
# 居中输出
print(a.center(80, '~'))
# 右对齐
print(a.rjust(80, '='))
# 左对齐
print(a.ljust(80, '='))

# 零填充
b = '123'
print(b.zfill(6))

# 以下三种语法的结构一致
c = 1234
d = 345
print('%d+%d=%d' % (c, d, c + d))
print(f'{c}+{d}={c + d}')
print('{}+{}={}'.format(c, d, c + d))
print('{0}+{1}={2}'.format(c, d, c + d))

# 具体的格式化字符串方法见markdown文件
