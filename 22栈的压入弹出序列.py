# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        i,j = 0,0
        stack = []
        while i < len(pushV):
            stack.append(pushV[i])
            if popV[j] == stack[-1]:   # 弹出序列当前值为栈顶元素
                i += 1
                j += 1
                stack.pop()
                while j < len(popV):
                    if popV[j] == stack[-1]:   # pop序列中一直弹出
                        j += 1
                        stack.pop()
                    else:
                        break
            else:                 # 不相等则入栈
                i += 1
        return True if len(stack) == 0 else False
        
    # 优化版本
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        i,j = 0,0
        stack = []
        while i < len(pushV):
            stack.append(pushV[i])
            while j < len(popV) and stack[-1] == popV[j]:
                stack.pop()
                j += 1
            i+=1
        return True if len(stack) == 0 else False
        

test = Solution()
pushV = "12345"
popV = "45321"
print(test.IsPopOrder(pushV,popV))