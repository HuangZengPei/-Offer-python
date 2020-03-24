class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in nums:      #依次异或
            temp ^= i
        num = 1
        while not (num & temp):      # 寻找从右往左第一位是1的数
            num <<= 1
        result1 = 0
        result2 = 0
        for i in nums:
            if num&i:               # 分成两个数组
                result1 ^= i
            else:
                result2 ^= i
        return [result1,result2]
        