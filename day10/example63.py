"""
example63 - 联网获取JSON格式的数据并解析出需要的内容

修改三方库的下载来源为国内的镜像网站（选用）---> pip config set global.index-url https://pypi.doubanio.com/simple
三方库 ---> requests --->pip install requests

协议 ---> 通信双方需要遵守的会话的规则。
    - http
    - https --->通过URL访问网络资源的协议---> Hyper-Text Transfer Protocol（超文本传输协议）

请求(request） -响应（response）

Author: larry
Date: 10/19/22

"""
import json

import requests

data = requests.get(
    url='http://api.tianapi.com/auto/index',
    params={'key': '8e8ee3267ff700f91a6f4f86c064cc10', 'num': 20})

# loads函数可以将JSON格式的数据转成Python中字典
# news_dict = json.loads(data.text)  # 下一句为简便写法，不需要调用json模块：
news_dict = data.json()
news_list = news_dict['newslist']
# print(news_list)
for news in news_list:
    print(news['title'], news['url'])
