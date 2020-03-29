# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,root,node,stack):
        if not root:return False
        stack.append(root)
        if node.val == root.val:
            return True
        if self.dfs(root.left,node,stack) or self.dfs(root.right,node,stack):
            return True
        stack.pop()
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:return None
        stackp = []
        stackq = []
        self.dfs(root,p,stackp)
        self.dfs(root,q,stackq)
        res = stackp[0]
        i = 0
        while i < len(stackp) and i < len(stackq) and stackp[i] == stackq[i]:
            res = stackp[i]
            i += 1
        return res
            