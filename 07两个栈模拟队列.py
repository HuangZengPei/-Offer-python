# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return
        if len(self.stack2) == 0:    # stack2为空，就把1中的所有加入到2中。不为空直接返回stack2的栈顶
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

class QueueToStack:  # 两个队列模拟栈
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, node):
        # write code here
        self.queue1.append(node)
    def pop(self):
        # return xx
        if len(self.queue1) == 0:return None
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1,self.queue2 = self.queue2,self.queue1
        return self.queue2.pop()
        
test = QueueToStack()
test.push(2)
test.push(3)
test.push(5)
print(test.pop())
print(test.pop())
print(test.pop())