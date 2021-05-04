#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>

# Problem 2
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from memory_profiler import profile


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def sum2numbers(self, l1: ListNode, l2: ListNode, is_carry) -> ListNode:
        if l1 is None and l2 is None:
            return ListNode(1) if is_carry else None
        if l2 is None:
            sum = l1.val
        elif l1 is None:
            sum = l2.val
        else:
            sum = l1.val + l2.val

        if is_carry:
            sum += 1

        node = ListNode(sum % 10)

        next_node = self.sum2numbers(l1.next if l1 else None, l2.next if l2 else None, sum > 9)

        node.next = next_node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.sum2numbers(l1, l2, False)

    def create_num_chain(self, l):
        chain = tail = None
        for n in l:
            new_node = ListNode(int(n))
            if chain is None:
                chain = tail = new_node
                chain.next = None
            else:
                tail.next = new_node
                tail = new_node
        return chain

    def print_chain(self, chain):
        # print(create_chain_num(chain))
        s = ''
        while chain is not None:
            s += str(chain.val)
            chain = chain.next
        print(s)


# @profile
def inspect(l1, l2):
    ds = Solution().addTwoNumbers(l1, l2)
    print(ds)


def run(target, nums):
    l = len(nums)
    for i, x in enumerate(nums):
        print(i, x)
        for j in range(i + 1, l):
            y = nums[j]
            print(j, y)
            if target == x + y:
                return i, j


if __name__ == "__main__":
    s = Solution()
    # S1
    chain_a = s.create_num_chain([2, 4, 3])
    s.print_chain(chain_a)
    chain_b = s.create_num_chain([5,6,4])
    s.print_chain(chain_b)
    chain_sum = s.addTwoNumbers(chain_a, chain_b)
    s.print_chain(chain_sum)
    # 708

    # S1
    chain_a = s.create_num_chain([2, 4, 5])
    s.print_chain(chain_a)
    chain_b = s.create_num_chain([5,6,5])
    s.print_chain(chain_b)
    chain_sum = s.addTwoNumbers(chain_a, chain_b)
    s.print_chain(chain_sum)
    # 7011

    # S2
    chain_a = s.create_num_chain([0])
    s.print_chain(chain_a)
    chain_b = s.create_num_chain([0])
    s.print_chain(chain_b)
    chain_sum = s.addTwoNumbers(chain_a, chain_b)
    s.print_chain(chain_sum)
    # 0

    # S3
    chain_a = s.create_num_chain([9, 9, 9, 9, 9, 9, 9])
    s.print_chain(chain_a)
    chain_b = s.create_num_chain([9, 9, 9, 9])
    s.print_chain(chain_b)
    chain_sum = s.addTwoNumbers(chain_a, chain_b)
    s.print_chain(chain_sum)
    # 89990001

    # S4
    # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    # [5, 6, 4]
    chain_a = s.create_num_chain(
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    s.print_chain(chain_a)
    chain_b = s.create_num_chain([5, 6, 4])
    s.print_chain(chain_b)
    chain_sum = s.addTwoNumbers(chain_a, chain_b)
    s.print_chain(chain_sum)
    # [6,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
