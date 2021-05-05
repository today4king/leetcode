#   Copyright 2021 jinzhao.me All rights reserved
#   #
#   Authors: Carry Jin <today4king@gmail.com>
#
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
        if len(array) == 0:
            return None
        head = ListNode(array[0])
        node = head
        for i in range(1, len(array)):
            node.next = ListNode(array[i])
            node = node.next
        return head

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        after = head.next
        head.next = after.next
        after.next = head
        head = after
        after = head.next
        while after.next is not None and after.next.next is not None:
            pre=after
            node = after.next
            after=node.next
            pre.next=after
            node.next=after.next
            after.next=node
            after=node
        return head


if __name__ == '__main__':
    solution = Solution()
    head = [1, 2, 3, 4]
    print(head)
    print(solution.node2array(solution.swapPairs(solution.array2node(head))))
    print('------------------')
    head = [1, 2, 3, 4,5]
    print(head)
    print(solution.node2array(solution.swapPairs(solution.array2node(head))))
    print('------------------')
    head = []
    print(head)
    print(solution.node2array(solution.swapPairs(solution.array2node(head))))
    print('------------------')
    head = [1]
    print(head)
    print(solution.node2array(solution.swapPairs(solution.array2node(head))))
    print('------------------')
