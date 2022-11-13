"""
example26 - 五人分鱼问题
五个人（ABCDE）晚上去捕鱼，捕了不计其数的鱼，然后累了去睡觉。
第二天，A第一个醒过来，把鱼分成了5份，扔掉了多余的1条，然后拿走自己的1份；
B第二个醒过来，以为鱼没有分过，把剩下的鱼分成了5份，扔掉了多余的1条，拿走自己的1份；
C、D、E依次醒过来，都按照同样的方法来分鱼。问他们最少捕了多少条鱼？
Author: larry
Date: 10/5/22

"""
print("A、B、C、D、E五人最少捕了：")
fish = 5
while True:
    all_take = 0
    enough = True
    for i in range(1, 6):
        if fish >= all_take and (fish - all_take) % 5 == 1:
            person_take = (fish - all_take) // 5
            abandon_fish = 1
            all_take += person_take + abandon_fish
        else:
            enough = False
            break

    if enough:
        print(f"{fish}条鱼")
        break
    fish += 1
