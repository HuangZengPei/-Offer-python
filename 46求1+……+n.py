class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        （1）如果多个变量均非0（包括None、False等），那么返回最后一个变量的值。如3 and 2 and 'a'的返回值为'a'；
        （2）如果多个变量中存在0值，则返回第一个0值。如1 and 'a' and 0 and None的返回值为0。
        """
        return n and n + self.sumNums(n-1)

print(Solution().sumNums(4))