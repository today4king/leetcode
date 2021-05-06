#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, c):
        self.stack.append(c)
        self.size += 1

    def pop(self):
        if self.size==0:
            return None
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.size == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        left_p = '({['

        right_p = ')}]'
        p_dic = {}
        for i, lp in enumerate(left_p):
            p_dic[lp] = right_p[i]
        for c in s:
            if c in left_p:
                stack.push(c)
                continue
            if stack.is_empty():
                return False
            last_input = stack.pop()
            if p_dic[last_input] == c:
                continue
            else:
                return False
        if stack.is_empty():
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = "()"
    print(s)
    print(solution.isValid(s) == True)
    print('---------------')
    s = "()[]{}"
    print(s)
    print(solution.isValid(s) == True)
    print('---------------')
    s = "(]"
    print(s)
    print(solution.isValid(s) == False)
    print('---------------')
    s = "([)]"
    print(s)
    print(solution.isValid(s) == False)
    print('---------------')
