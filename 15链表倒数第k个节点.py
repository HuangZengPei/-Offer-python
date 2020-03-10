# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:return None
        p1 = head
        for i in range(k-1):
            if p1.next :
                p1 = p1.next
            else:
                return None
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2