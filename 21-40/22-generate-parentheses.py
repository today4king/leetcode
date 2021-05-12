#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
from typing import List
from collections import deque


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, c):
        self.stack.append(c)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.size == 0


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lp = '('
        rp = ')'
        ret = []

        def gpTree(cur_s, left, right):
            if left == 0 and right == 0:
                ret.append(cur_s)
                return
            if right < left:
                return
            if left > 0:
                gpTree(cur_s + lp, left - 1, right)
            if right > 0:
                gpTree(cur_s + rp, left, right - 1)

        gpTree('', n, n)
        return ret


if __name__ == '__main__':
    solution = Solution()
    n = 3
    print(n)
    print(solution.generateParenthesis(n))
    print('---------------')
    n = 1
    print(n)
    print(solution.generateParenthesis(n))
    print('---------------')
