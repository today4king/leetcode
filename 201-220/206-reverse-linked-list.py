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
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pre = None
        while head.next is not None:
            after = head.next

            head.next = pre
            pre = head
            if after.next is None:
                after.next = head
                head = after
                return head
            head = after
            after = after.next

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


solution = Solution()
head = [1, 2]
print(head)
head = solution.array2node(head)
print(solution.node2array(solution.reverseList(head)))

head = []
print(head)
head = solution.array2node(head)
print(solution.node2array(solution.reverseList(head)))

head = [1, 2, 3, 4, 5]
print(head)
head = solution.array2node(head)
print(solution.node2array(solution.reverseList(head)))
