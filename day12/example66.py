"""
example66 - 获取A班和B班的考试成绩的描述性统计信息，
比较A班和B班哪个班的学习效果更理想。

Author: larry
Date: 10/29/22

"""
import random

from homework23 import ptp, average, var, std, med

class_a_scores = [random.randint(60, 100) for _ in range(50)]
class_b_scores = [random.randint(60, 100) for _ in range(50)]
print(f"A班成绩：{class_a_scores}。")
print("A班考试成绩描述性统计信息：")
print(
    f"极差：{ptp(class_a_scores)}、平均数：{average(class_a_scores)}、方差：{var(class_a_scores)}、标准差：{std(class_a_scores)}、中位数：{med(class_a_scores)}。")
print(f"B班成绩：{class_b_scores}。")
print("B班考试成绩描述性统计信息：")
print(
    f"极差：{ptp(class_b_scores)}、平均数：{average(class_b_scores)}、方差：{var(class_b_scores)}、标准差：{std(class_b_scores)}、中位数：{med(class_b_scores)}。")
