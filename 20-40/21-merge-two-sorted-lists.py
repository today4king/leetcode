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
    def __str__(self):
        return str(self.val)


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

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val >= l2.val:
            head = l2
            node = head
            l2 = l2.next
            node.next=None
        else:
            head = l1
            node = head
            l1 = l1.next
            node.next=None
        while l1 is not None or l2 is not None:
            if l1 is None:
                node.next = l2
                node = l2
                l2 = l2.next
                node.next=None
            elif l2 is None:
                node.next = l1
                node = l1
                l1 = l1.next
                node.next = None
            else:
                if l1.val >= l2.val:
                    node.next = l2
                    node = l2
                    l2 = l2.next
                    node.next = None
                else:
                    node.next = l1
                    node = l1
                    l1 = l1.next
                    node.next = None
        return head


if __name__ == '__main__':
    solution = Solution()
    a1 = [1, 2, 4]
    a2 = [1, 3, 4]
    print(a1)
    print(a2)
    a1 = solution.array2node(a1)
    a2 = solution.array2node(a2)
    print(solution.node2array(solution.mergeTwoLists(a1, a2)))
    print('-----------------')
    a1 = []
    a2 = []
    print(a1)
    print(a2)
    a1 = solution.array2node(a1)
    a2 = solution.array2node(a2)
    print(solution.node2array(solution.mergeTwoLists(a1, a2)))
    print('-----------------')
    a1 = []
    a2 = [0]
    print(a1)
    print(a2)
    a1 = solution.array2node(a1)
    a2 = solution.array2node(a2)
    print(solution.node2array(solution.mergeTwoLists(a1, a2)))
    print('-----------------')
