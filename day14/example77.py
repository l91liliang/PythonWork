'''
Author: l91liliang l91liliang@gmail.com
Date: 2022-11-05 16:54:37
LastEditors: l91liliang l91liliang@gmail.com
LastEditTime: 2022-11-05 17:22:14
FilePath: /PythonWork/day14/example77.py
Description: example77 - 创建一个时钟的对象（可以显示时/分/秒），让它运转起来（走字）
'''
import time
import os


class DigitalClock:
    """时钟"""

    def __init__(self, *, hour=0, minute=0, second=0) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'

    def run(self):
        """走字"""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0


if __name__ == '__main__':
    clock1 = DigitalClock(hour=23, minute=59, second=55)
    while True:
        print(clock1.show())
        time.sleep(1)
        os.system('clear')
        clock1.run()
