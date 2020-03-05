# -*- coding:utf-8 -*-
class Solution:
    # 快速幂的非递归写法
    def Power(self, base, exponent):
        # write code here
        isNegetive = False
        if exponent < 0:
            isNegetive = True
            exponent = abs(exponent)
        if base == 0:return 0
        ans = 1.0
        while exponent > 0:
            if exponent & 1 == 1:
                ans = ans * base
            exponent >> 1
            base *= base
        return 1/ans if isNegetive else ans
        
        
    # 递归求快速幂
    def Power(self, base, exponent):
        # write code here
        if base == 0:return 0
        if exponent == 0:
            return 1
        if exponent > 0:
            return self.PowerValue(base,exponent)
        else:
            return 1/self.PowerValue(base,abs(exponent))
            
    def PowerValue(self, base, exponent):
        # write code here
        if exponent == 1:return base
        if exponent & 1 == 0:
            return self.PowerValue(base,exponent>>1) ** 2
        else:
            return self.Power(base,(exponent-1)>>1)**2 * base
            
test = Solution()
print(test.Power(0,1))
            