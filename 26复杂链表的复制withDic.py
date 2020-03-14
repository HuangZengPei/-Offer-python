# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:return None
        newHead = RandomListNode(0)  # 新初始化个表头
        dic = {}      # 使用字典保存新-旧映射
        new = newHead
    
        while pHead:
            newHead.next = RandomListNode(pHead.label)
            dic[newHead.next] = pHead
            pHead = pHead.next
            newHead = newHead.next
    
        new = new.next
        n = new
    
        while new:
            new.random = dic[new].random
            new = new.next
        return n
            
            