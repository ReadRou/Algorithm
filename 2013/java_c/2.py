# coding : utf-8
# Author : Luoxh
# Date   : 2019/11/14 下午6:06
# IDE    : PyCharm
# Project: Algorithm
# Name   : 2.py
# Created by Luoxh on 下午6:06.
# Copyright © 2019 Luoxh. All rights reserved.

# 标题: 组素数
#
#     素数就是不能再进行等分的数。比如：2 3 5 7 11 等。
#     9 = 3 * 3 说明它可以3等分，因而不是素数。
#
#     我们国家在1949年建国。如果只给你 1 9 4 9 这4个数字卡片，可以随意摆放它们的先后顺序（但卡片不能倒着摆放啊，我们不是在脑筋急转弯！），那么，你能组成多少个4位的素数呢？
#
#     比如：1949，4919 都符合要求。
#
#
# 请你提交：能组成的4位素数的个数，不要罗列这些素数!!
#
# 注意：不要提交解答过程，或其它的辅助说明文字。

# 素数判定，素数生成（筛法），质因数分解
# 全排列+检查

def f(arr, k):
    """
    全排列的固定写法，用于交换，生成新的数据，保证可以生成全部所需要的数据
    :param arr: 需要处理的数组
    :param k: 处理到了第几位
    :return: 返回所需要的数据
    """
    for i in range(0, 4):
        t = arr[k]
        arr[k] = arr[i]
        arr[i] = t
        f(arr, k + 1)
        t = arr[k]
        arr[k] = arr[i]
        arr[i] = t


if __name__ == '__main__':
    result = 0
