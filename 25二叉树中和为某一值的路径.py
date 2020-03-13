# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def __init__(self):
        self.onePath = []
        self.PathArray = []
        
    def FindPath(self, root, expectNumber):
        if root is None:
            return self.PathArray
        self.onePath.append(root.val)
        expectNumber -= root.val
        if expectNumber==0 and not root.left and not root.right:
            self.PathArray.append(self.onePath[:])
        elif expectNumber>0:
            self.FindPath(root.left,expectNumber)
            self.FindPath(root.right,expectNumber)
        expectNumber += root.val
        self.onePath.pop()
        return self.PathArray


        
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
left = root.left
left.left = TreeNode(4)
left.right = TreeNode(7)

test = Solution()
res = test.FindPath(root,22)
print(res)