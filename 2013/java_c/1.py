# coding : utf-8
# Author : Luoxh
# Date   : 2019/11/14 下午5:57
# IDE    : PyCharm
# Project: Algorithm
# Name   : 1.py
# Created by Luoxh on 下午5:57.
# Copyright © 2019 Luoxh. All rights reserved.

# 标题: 猜年龄
#
#
#     美国数学家维纳(N.Wiener)智力早熟，11岁就上了大学。他曾在1935~1936年应邀来中国清华大学讲学。
#
#     一次，他参加某个重要会议，年轻的脸孔引人注目。于是有人询问他的年龄，他回答说：
#
#     “我年龄的立方是个4位数。我年龄的4次方是个6位数。这10个数字正好包含了从0到9这10个数字，每个都恰好出现1次。”
#
#     请你推算一下，他当时到底有多年轻。
#
#     通过浏览器，直接提交他那时的年龄数字。
#     注意：不要提交解答过程，或其它的说明文字。

# 解法：很简单的数学题
def check(check_result):
    # 声明一个结果set，用于保存遍历出来的字符串，去重
    result = set()
    for item in check_result:
        result.add(item)
    # 如果满足0-9，则长度为10
    return len(result) == 10


if __name__ == '__main__':
    # 从10岁开始，99岁结束，因为人的寿命不可能超过100岁，而且世界的数学大会也不可能小于10就参加
    for i in range(10, 100):
        # 岁数的立方
        i1 = i * i * i
        # 岁数的四次方
        i2 = i * i * i * i
        # 转出字符串，用于添加到set，来确定是否是从0-9
        s1 = str(i1)
        s2 = str(i2)
        # 做判断如果符合 长度为4，以及长度为6，才去check，节省内存
        if len(s1) == 4 and len(s2) == 6 and check(s1 + s2):
            print(i)
            break
