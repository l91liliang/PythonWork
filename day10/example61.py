"""
example61 - 在一个字典中保存了股票的代码和价格，完成下面的操作：
1.找出股票价格大于100元的股票并创建一个新的字典
2.找出价格最高和最低的股票对应的股票代码
3.按照股票价格从高到低给股票代码排序



Author: larry
Date: 10/19/22

"""
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# 任务1：找出股票价格大于100元的股票并创建一个新的字典
# stocks_over_100 = {}
# for key, value in stocks.items():
#     if value > 100:
#         stocks_over_100[key] = value # 这种方法写起来太麻烦

stocks_over_100 = {key: value for key, value in stocks.items() if value > 100}  # 这种方法写起来比较美观

print(stocks_over_100)

# 任务2：找出价格最高和最低的股票对应的股票代码
# max_stockid, max_stockvalue = '', 0
# min_stockid, min_stockvalue = '', float('inf')
# for key, value in stocks.items():
#     if value > max_stockvalue:
#         max_stockid = key
#         max_stockvalue = value
#
#     if value < min_stockvalue:
#         min_stockid = key
#         min_stockvalue = value
#
# print(f'最高价股票代码：{max_stockid}，股价{max_stockvalue}')
# print(f'最低价股票代码：{min_stockid}，股价{min_stockvalue}')#此方法太复杂

# 简便写法
# print(
#     f'最高价的股票是{max(zip(stocks.values(), stocks.keys()))[1]},价格为{max(zip(stocks.values(), stocks.keys()))[0]}。')
#
# print(
#     f'最低价的股票是{min(zip(stocks.values(), stocks.keys()))[1]},价格为{min(zip(stocks.values(), stocks.keys()))[0]}。')

# 最佳简便写法
print(f'最高价的股票是{max(stocks, key=stocks.get)}。')
print(f'最低价的股票是{min(stocks, key=stocks.get)}。')

# 任务3：按照股票价格从低到高/从高到低给股票代码排序
print(f'股票价格从低到高的顺序是{sorted(stocks, key=stocks.get, reverse=False)}')
print(f'股票价格从高到低的顺序是{sorted(stocks, key=stocks.get, reverse=True)}')
