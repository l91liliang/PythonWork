"""
example56 - 字典

Author: larry
Date: 10/18/22

"""
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}  # 键-值对
print(xinhua['麓'])

person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877',
    'favorites': ['唱', '跳', 'Rap', '篮球'],  # 可在字典中放入集合
    'contacts': {
        'QQ': '123456',
        'email': 'l91liliang@163.com',
        'tel': '18888888888'
    }  # 可在字典中放入字典
}
print(person['name'])
print(person['favorites'])
for fav in person['favorites']:
    print(fav)
print(person['contacts']['tel'])
