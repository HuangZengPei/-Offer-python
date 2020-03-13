# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:return
        que = Queue()
        result = []
        que.put(root)
        while not que.empty():
            node = que.get()
            result.append(node.val)
            if node.left:
                que.put(node.left)
            if node.right:
                que.put(node.right)
        return result