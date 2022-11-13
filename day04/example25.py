"""
example25 - 百钱百鸡问题（穷举法、暴力搜索法）

鸡翁一值钱5，鸡母一值钱3，鸡雏三值钱1，用百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

Author: larry
Date: 10/5/22

"""
print("百钱百鸡问题：")
a = 0
b = 0
c = 0
i = 1
for a in range(0, 21):  # 100元最多买20只鸡翁，提高运行效率
    for b in range(0, 34):  # 100元最多买33只鸡母，提高运行效率
        c = 100 - a - b
        flag1 = 5 * a + 3 * b + c / 3 == 100
        flag2 = c % 3 == 0
        if flag1 and flag2:
            print(f"解法{i}：鸡翁{a}只，鸡母{b}只，鸡雏{c}只。")
            i += 1
