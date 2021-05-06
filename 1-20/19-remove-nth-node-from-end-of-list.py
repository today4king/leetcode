#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def node2array(self, head: ListNode):
        if head is None:
            return []
        array = [head.val]
        while head.next is not None:
            head = head.next
            array.append(head.val)
        return array

    def array2node(self, array: List):
        head = ListNode(array[0])
        node = head
        for i in range(1, len(array)):
            node.next = ListNode(array[i])
            node = node.next
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 1
        pre = node = head
        while node is not None:
            if i > n + 1:
                pre = pre.next
            node = node.next
            i += 1
        i -= 1
        if i < n:
            return []
        elif i == n:
            head = head.next
        elif n == 1:
            pre.next = None
        else:
            pre.next = pre.next.next
        return head


if __name__ == '__main__':
    solution = Solution()
    # head = solution.array2node([1, 2, 3, 4, 5])
    # print(solution.node2array(solution.removeNthFromEnd(head, 2)))
    # print('-------------------')
    head = solution.array2node([1, 2, 3, 4, 5])
    print(solution.node2array(solution.removeNthFromEnd(head, 4)))
    print('-------------------')
    head = solution.array2node([1, 2, 3, 4, 5])
    print(solution.node2array(solution.removeNthFromEnd(head, 3)))
    print('-------------------')
    head = solution.array2node([1, 2, 3, 4, 5])
    print(solution.node2array(solution.removeNthFromEnd(head, 2)))
    print('-------------------')
    head = solution.array2node([1])
    print(solution.node2array(solution.removeNthFromEnd(head, 1)))
    print('-------------------')
    head = solution.array2node([1, 2])
    print(solution.node2array(solution.removeNthFromEnd(head, 1)))
    print('-------------------')
