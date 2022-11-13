"""
example14 - 分段函数求值
     3x-5(x>1)
f(x)=x+2(-1<=x<=1)
     5x+3(x<-1)
分支结构可以嵌套使用，但是一定要注意嵌套的深度，嵌套深度太深直接影响代码的可读性
Python里面的代码块：保持相同的缩进代码就属于同一个代码块。

Author: larry
Date: 10/2/22

"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')
