"""
example60 - 输入一段话，统计每个英文字母出现的次数

Author: larry
Date: 10/19/22

"""
sentence = '5LiN6KaB5qC46YW46KaB5ZCD6aWt77yM5LiN6KaB5bCB6ZSB6KaB6Ieq55SxLOS4jeimgeiwjuiogOimgeWwiuS4pe+8jOS4jeimgeaWh+mdqeimgeaUuemdqSzkuI3opoHpooboopbopoHpgInnpajvvIzkuI3lgZrlpbTmiY3lgZrlhazmsJEs572i6K++572i5bel572i5YWN54us6KOB5Zu96LS85Lmg6L+R5bmz'
counter = {}
for en in sentence:
    if 'A' <= en <= 'Z' or 'a' <= en <= 'z':
        counter[en] = counter.get(en, 0) + 1

for key, value in counter.items():
    print(f'输入的句中，字母{key}出现了{value}次')
