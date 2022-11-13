#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example72.py - 二分查找
@Time    :   2022/10/31 22:08:55
@Author  :   Larry 
@Version :   1.0
@Contact :   l91liliang@hotmail.com
@License :   
@Desc    :   None
'''


def bin_search(items: list, key) -> int:
    """
    二分查找（渐近时间复杂度O(log2 n)）

    :param items： 待查找的列表（列表有序，升序）
    :param key：要找的元素
    :return ： 找到了返回元素的索引，找不到返回-1

    """
    start, end = 0, len(items)-1
    while start <= end:
        mid = (start+end)//2
        if key > items[mid]:
            start = mid+1
        elif key < items[mid]:
            end = mid-1
        else:
            return mid
    return -1


if __name__ == '__main__':
    nums = [1, 3, 5, 7, 9, 11, 13, 15]
    print(bin_search(nums, 10))
    print(bin_search(nums, 11))
