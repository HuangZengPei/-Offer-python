# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here\
        result = [0,1]
        if n < 0:return None
        if n <= 1:
            return result[n]
        fibonaciOne = 0
        fibonaciTwo = 1
        fibonaciN = 0
        for i in range(2,n+1):
            fibonaciN = fibonaciOne + fibonaciTwo
            fibonaciOne = fibonaciTwo
            fibonaciTwo = fibonaciN
        return fibonaciN
        
test = Solution()
print(test.Fibonacci(6))