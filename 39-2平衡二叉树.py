# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def maxDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root == None:return 0
    #     left = self.maxDepth(root.left)
    #     right = self.maxDepth(root.right)
    #     return max(left+1,right+1)
    # 
    # # 简单的方法
    # def isBalanced(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root == None:return True
    #     left = self.maxDepth(root.left)
    #     right = self.maxDepth(root.right)
    #     diff = abs(left-right)
    #     if diff > 1:
    #         return False
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    # 后序遍历
    def balance(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return 0 
        lHeight = self.balance(root.left)
        rHeight = self.balance(root.right)
        # 左右子树是否平衡
        if lHeight<0 or rHeight < 0:
            return -1
        if abs(lHeight - rHeight) <= 1:
            curHeight = max(lHeight, rHeight) + 1
            return curHeight
        else:
            return -1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if self.balance(root)>= 0 else False
        