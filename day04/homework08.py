"""
homework08 - 输入三角形三条边的长度，如果能构成三角形就计算周长和面积，
如果不能构成三角形，提示用户重新输入，直到正确。
已知三边求三角形面积的公式：海伦公式——S=sqrt(s*(s-a)*(s-b)*(s-c))其中s=(a+b+c)/2
Author: larry
Date: 10/4/22

"""
from math import sqrt as sqrt

while True:
    a = float(input("请输入三角形的第一条边："))
    b = float(input("请输入三角形的第二条边："))
    c = float(input("请输入三角形的第三条边："))
    flag1 = a + b > c
    flag2 = b + c > a
    flag3 = a + c > b
    if flag1 and flag2 and flag3:
        perimeter = a + b + c
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"由{a}、{b}、{c}三条边构成的三角形周长为{perimeter}，面积为{area}。")
        break
    else:
        print(f"由{a}、{b}、{c}三条边无法构成三角形，请重新输入：")
        continue
