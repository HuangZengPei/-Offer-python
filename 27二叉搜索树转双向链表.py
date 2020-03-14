# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def Convert(self, root):
        if not root:
            return
        self.Convert(root.left)
        if not self.head:
            self.head, self.tail = root, root
        else:
            #前一个尾节点的右孩子指向当前根节点，即双向链表中的后向指针next
            #当前根节点的左孩子指向前一个尾节点，即前向指针prev
            self.tail.right, root.left = root, self.tail
            self.tail = self.tail.right   #更新尾节点
        self.Convert(root.right)
        return self.head
            