# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 计算的是补码中1的个数
        count = 0
        if n < 0:
            n = n & 0xffffffff
            # Python中的整型是补码形式存储的
            # Python中bin一个负数（十进制表示），输出的是它的原码的二进制表示加上个负号，方便查看（方便个鬼啊）
            # Python中bin一个负数（十六进制表示），输出的是对应的二进制表示。（注意此时）
            # 所以你为了获得负数（十进制表示）的补码，需要手动将其和十六进制数0xfffffffd进行按位与操作，得到结果也
            # 是个十六进制数，再交给bin()进行输出，得到的才是你想要的补码表示。
        while n!=0:
            count += 1
            n = (n-1)&n
        return count
        
print(bin(-5))
print(bin(-5 & 0xffffffff))