"""
homework19 - 输入一个英文的句子，统计每个单词出现的次数。

Author: larry
Date: 10/21/22

"""
sentence = input('请输入英文句子：').lower()
words = sentence.replace(',', '').replace('.', '').replace(':', '').split()

# 统计每个单词出现的次数：
counter_dict = {}
for word in words:
    counter_dict[word] = counter_dict.get(word, 0) + 1

# 根据单词出现的次数从高到低排列：
sorted_keys = sorted(counter_dict, key=counter_dict.get, reverse=True)
for key in sorted_keys:
    print(f'{key}出现了{counter_dict[key]}次。')
