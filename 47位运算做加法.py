class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a &= 0xffffffff       # python 因为位数没有限制，所以负数补码会很长，所以要位与 0xffffffff 处理成 3232 位整型数。
        b &= 0xffffffff
        while b != 0:
            carry = ((a & b) << 1) & 0xffffffff
            a ^= b
            b = carry
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
        
print(Solution().add(5,7))
        