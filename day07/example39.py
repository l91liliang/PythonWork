"""
example39 - 保存5个学生，3门课程的成绩

Author: larry
Date: 10/10/22

"""
import random

names = ['A', 'B', 'C', 'D', 'E']
courses = ['语文', '数学', '英语']

scores = [[random.randrange(60, 101) for _ in range(len(courses))] for _ in range(len(names))]  # 随机嵌套列表的生成。
# for i, name in enumerate(names):
#     for j, course in enumerate(courses):
#         print(f'{name}的{course}成绩：{scores[i][j]}')


# 统计每个学生的平均成绩
for i, name in enumerate(names):
    print(f"{name}的平均成绩：{sum(scores[i]) / len(courses):.2f}")
# 统计每门课的最高分、最低分
for j, course in enumerate(courses):
    temp = [scores[i][j] for i in range(len(names))]
    print(f"{course}的最高分是{max(temp)}，最低分是{min(temp)}。")
