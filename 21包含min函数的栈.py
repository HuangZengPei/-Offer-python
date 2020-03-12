# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        # 辅助栈存放最小的数值以及次小的数值
        self.minStack = []
    
    def push(self, node):
        # write code here
        self.stack.append(node)
        
        if len(self.minStack) == 0 or node < self.minStack[-1]:
            self.minStack.append(node)
        else:
            self.minStack.append(self.minStack[-1])
            
    def pop(self):
        # write code here
        # pop的时候两个栈都要入栈
        if len(self.stack) > 0 and len(self.minStack) > 0:
            self.stack.pop()
            self.minStack.pop()
        else:
            return None
        
            
    def top(self):
        # write code here
        return self.stack[-1]
        
    def min(self):
        # write code here
        if len(self.stack) > 0 and len(self.minStack) > 0:
            return self.minStack[-1]