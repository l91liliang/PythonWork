"""
homework01 - 输入圆的半径，计算圆的周长和面积

Author: larry
Date: 10/2/22

"""
import math

r = float(input('请输入圆的半径：'))
c = 2 * r * math.pi
s = r ** 2 * math.pi
print(f"半径为{r}的圆，周长为{c:.2f}，面积为{s:.2f}。")  # 输出时保留两位小数。
