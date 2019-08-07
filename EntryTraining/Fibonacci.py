#
#   Fibonacci.py
#   Algorithm
#
#   Created by luoxh on 2019/8/7 - 16:46.
#   Copyright © 2019 luoxh. All rights reserved.
#


M = 10007
RESULT = 0
if __name__ == '__main__':
    a1 = a2 = 1
    n = int(input())
    for i in range(1, n + 1):
        RESULT = a1 % M
        tmp = a2
        a2 = (a1 + a2) % M
        a1 = tmp
    print(RESULT)
