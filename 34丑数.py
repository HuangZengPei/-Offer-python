# -*- coding:utf-8 -*-
class Solution:
# 运行时间：28ms
# 占用内存：5856k
    def GetUglyNumber_Solution(self, index):
        if index == 0:return 0
        uglyNumbers = [0 for i in range(index)]
        uglyNumbers[0] = 1
        count = 1
        p2Index, p3Index, p5Index = 0,0,0
        # 不需要每个数都乘1遍，只需要找到临界的p2,p3,p5
        while count < index:
            minUglyNumber = min(uglyNumbers[p2Index] *2 ,uglyNumbers[p3Index]*3,uglyNumbers[p5Index]*5)
            uglyNumbers[count] = minUglyNumber
            while uglyNumbers[p2Index] *2 <= uglyNumbers[count]:
                p2Index += 1
            while uglyNumbers[p3Index] *3 <= uglyNumbers[count]:
                p3Index += 1
            while uglyNumbers[p5Index] *5 <= uglyNumbers[count]:
                p5Index += 1
            count += 1
        result = uglyNumbers[index-1]
        return result
        
test = Solution()
print(test.GetUglyNumber_Solution(20))
        