#  Copyright 2021 jinzhao.me All rights reserved
#  #
#  Authors: Carry Jin <today4king@gmail.com>
class ListNode:
    def __init__(self, key, val=None, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache:

    def __init__(self, capacity: int):
        self._dic = {}
        self._max_capacity = capacity
        self._cur_capacity = len(self._dic)
        self._head = None
        self._tail = None

    def update_use(self, node) -> None:
        if self._max_capacity > 1 and node is not self._head:
            if node is self._tail:
                self._tail = node.pre
                self._tail.next = None

            else:
                node.next.pre = node.pre
                node.pre.next = node.next
            node.next = self._head
            self._head.pre = node
            node.pre = None
            self._head = node

    def get(self, key: int) -> int:
        if key not in self._dic:
            return -1
        else:
            node = self._dic[key]
            self.update_use(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if self._head is None:
            self._head = ListNode(key, value)
            self._tail = self._head
            self._dic[key] = self._head
            self._cur_capacity = 1
            return None
        else:
            if self._cur_capacity >= self._max_capacity and key not in self._dic:
                if self._head is self._tail:
                    self._head = None
                    self._tail = None
                    self._dic = {}
                else:
                    del self._dic[self._tail.key]
                    self._tail = self._tail.pre
                    self._tail.next.pre = None
                    self._tail.next = None

        if key not in self._dic:
            node = ListNode(key, value)
            self._dic[key] = node
            self._cur_capacity = len(self._dic)
            if self._head is None:
                self._head = node
                self._tail = node
            else:
                node.next = self._head
                self._head.pre = node
                self._head = node
        else:
            node = self._dic[key]
            node.val = value
            self.update_use(node)
        return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
# print(lRUCache.put(1, 1))  # cache is {1=1}
# print(lRUCache.put(2, 2))  # cache is {1=1, 2=2}
# print(lRUCache.get(1))  # return 1
# print(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2))  # returns -1 (not found)
# print(lRUCache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(1))  # return -1 (not found)
# print(lRUCache.get(3))  # return 3
# print(lRUCache.get(4))  # return 4
#
# lRUCache = LRUCache(1)
# print(lRUCache.put(2, 1))
# print(lRUCache.get(2))
# print(lRUCache.put(3, 2))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
print('[null,-1,null,-1,null,null,2,6]')
lRUCache = LRUCache(2)
print(lRUCache.get(2))  # cache is {1=1}
print(lRUCache.put(2, 6))  # cache is {1=1, 2=2}
print(lRUCache.get(1))  # return 1
print(lRUCache.put(1, 5))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.put(1, 2))  # returns -1 (not found)
print(lRUCache.get(1))  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(2))  # return -1 (not found)
