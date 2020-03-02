# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0]) # 根节点在后序遍历中的位置
        
        root.left = self.reConstructBinaryTree(pre[1:val+1],tin[:val])  # 左子树的前序，后序遍历
        root.right = self.reConstructBinaryTree(pre[val+1:],tin[val+1:])
        return root