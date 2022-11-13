"""
example62 - JSON格式的字符串

操作系统：Windows、iOS、Android、macOS、Linux、Unix
编程语言：Python、Java、PHP、Go、C++

1. 两个异构的系统之间交换数据最好的选择是交换纯文本（可以屏蔽系统和编程语言的差异）
2. 纯文本应该是结构化或半结构化的纯文本（有一定的格式）
    - XML ---> 可扩展标记语言eXtensible Markup Language ---> 格式比较笨重
    - JSON ---> JavaScript Object Notation ---> 大多数网站和数据接口服务使用的数据格式
    - YAML ---> Yet Another Markup Language
3. 如何将JSON格式转换成Python程序中的字典
    ---> json 模块 ---> loads


Author: larry
Date: 10/19/22
"""
import json

data = '''
{
  "code": 200,
  "msg": "success",
  "newslist": [
    {
      "id": "14cd49c1fd6a2a1ff052b5c041ae2599",
      "ctime": "2022-10-19 17:00",
      "title": "配“眯眯眼”大灯 劳斯莱斯闪灵发布 续航或超585公里",
      "description": "明年交付劳斯莱斯闪灵发布零百4.5秒堪称电车“天花板”",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_25636d9533be41f2829689267badba4e.jpg",
      "url": "http://www.chexun.com/2022-10-19/113783039.html"
    },
    {
      "id": "063e740d426aadd8d62cac900dd8daf1",
      "ctime": "2022-10-19 17:00",
      "title": "重新站在起点的极星，这次到底想清楚了没有？",
      "description": "谈不上“哀其不幸，怒其不争”，但失望总归是有的",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_8b0901e9de374da583adcbd4304d9c7c.jpeg",
      "url": "http://www.chexun.com/2022-10-19/113783053.html"
    },
    {
      "id": "9c76c649436bd49d640590bcaafd0e4f",
      "ctime": "2022-10-19 17:00",
      "title": "试驾宋Pro DM-i，除了DM-i，还有更值得选它的理由",
      "description": "DM-i混动系统的魅力相信大家都已经非常了解了，出色的燃油经济性以及可油可电的用车场景的确戳中了消费者的用车痛点",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_9380182e404f4c26a137362ea048b040.jpg",
      "url": "http://www.chexun.com/2022-10-19/113783075.html"
    },
    {
      "id": "ab5368c2b98aaf10bfd1005f4557a558",
      "ctime": "2022-10-19 17:00",
      "title": "欧拉品牌全球化加速，闪电猫登陆巴黎车展",
      "description": "作为世界五大车展之一的巴黎车，国内外汽车品牌云集，一直被誉为行业“风向标”，能和众多百年汽车品牌同台竞技，欧拉汽车需要的不仅是勇气，更重要的实力，而闪电猫就是一款极具代表性的车型。",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_d518308e28af4b6cb7f48b8e5dfc649d.jpg",
      "url": "http://www.chexun.com/2022-10-19/113783077.html"
    },
    {
      "id": "66d84b2b8fe39e8751e662ecdbd2859a",
      "ctime": "2022-10-19 17:00",
      "title": "换壳再对决，传祺M8用上丰田混动，比DM-i的腾势D9更好吗？",
      "description": "传祺M8PHEV即将推出，将搭载2.0T+丰田THS混动，那么在面对腾势D9这样的插混MPV对手时，到底谁更值得买呢？",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_dae1528f5d8d46209fe5be716db30322.png",
      "url": "http://www.chexun.com/2022-10-19/113783099.html"
    },
    {
      "id": "281e1d28f242cb30155fd034614fd958",
      "ctime": "2022-10-19 16:00",
      "title": "比亚迪前三季度净利润同比预增近3倍",
      "description": "10月18日，比亚迪发布2022年前三季度业绩预告。预计今年前三季度归母净利润为91亿元至至95亿元，同比增加272.48%至288.85%；其中今年第三季度归母净利润预计为55.05亿元至59.05亿元，同比增加333.60%至365.11%。",
      "source": "车讯网",
      "picUrl": "http://i0.chexun.net/images/2022/1019/60293/news_default_99E7BA4883640A234ED2DF35F5B5B43E.jpg",
      "url": "http://www.chexun.com/2022-10-19/113783067.html"
    },
    {
      "id": "9f32e6bffe8ea392694996921b851c2f",
      "ctime": "2022-10-19 16:00",
      "title": "谁说华为智舱专供纯电车？“智能大魔王”北汽魔方上市9.99万起！",
      "description": "谁说华为智舱专供纯电车？“智能大魔王”北汽魔方上市9.99万起！",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_c902a632ef3d46bc8886d86a1e2e72ea.png",
      "url": "http://www.chexun.com/2022-10-19/113783025.html"
    },
    {
      "id": "793ce8fc56f6032085e3b45cff6f0677",
      "ctime": "2022-10-19 16:00",
      "title": "超豪华电动超级轿跑车，劳斯莱斯首款纯电动车 “闪灵”发布",
      "description": "超豪华电动超级轿跑车，劳斯莱斯首款纯电动车“闪灵”发布",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_43d6925f313547aa99473c5425fc6c6f.png",
      "url": "http://www.chexun.com/2022-10-19/113783027.html"
    },
    {
      "id": "e0af72d70919e3033bb32b8565e20156",
      "ctime": "2022-10-19 16:00",
      "title": "诺基亚要在月球上安装4G网络？",
      "description": "诺基亚的月球-LTE雄心是与美国国家航空航天局（NASA）签订的合同，旨在解决一个真实的地球之外的问题：现有的数据系统无法随着设备数量的增加而扩展。总有一天，人们会到月球这个距离地球约363300千米的地方工作。",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_07e289c83ade4471a78f42eabf1dafa1.jpg",
      "url": "http://www.chexun.com/2022-10-19/113783047.html"
    },
    {
      "id": "223e6edc474ad3349b010743734f4aac",
      "ctime": "2022-10-19 16:00",
      "title": "关于电动车电池，我们不知道的还有很多",
      "description": "电动汽车的电池性能在高温天气下会有怎样的变化？天气寒冷情况下又如何呢？如果有些电动汽车司机的驾驶风格过于狂野，对电池寿命有影响吗？电池材料的变化，对电动汽车在各种条件下的表现又会有什么改变？",
      "source": "车讯网",
      "picUrl": "https://img1.chexun.com/chexunimg/erpimg/2022/1019/icon_0_0_f6d49f7af15c4faf948f95d3c04587bb.jpg",
      "url": "http://www.chexun.com/2022-10-19/113783057.html"
    }
  ]
}



'''

# loads函数可以将JSON格式的数据转成Python中字典
news_dict = json.loads(data)
news_list = news_dict['newslist']
# print(news_list)
for news in news_list:
    print(news['title'], news['url'])
