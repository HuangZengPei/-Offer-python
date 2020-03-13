# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:return False
        root = sequence[-1]
        seq_len = len(sequence)
        i = 0
        # 二叉搜索树左子树小于根节点
        while i < seq_len - 1:
            if sequence[i] > root:
                break
            i += 1
        
        j = i
        # 右子树大于根节点
        while j < seq_len - 1:
            if sequence[j] < root:
                return False
            j += 1
            
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < seq_len - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        
        return left and right
        
test = Solution()
seq = [4,8,6,12,16,14,10]
print(test.VerifySquenceOfBST(seq))