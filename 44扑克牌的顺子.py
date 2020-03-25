class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) != 5:return False
        numberOf0 = 0
        numberOfGap = 0
        nums.sort()
        i = 0
        while nums[i] == 0:
            numberOf0 += 1
            i += 1
        i += 1   # i 指向第一个不为0的数，向后移一位
        while i < len(nums):
            if nums[i] == nums[i-1]:
                return False
            if nums[i] - nums[i-1] != 1:
                numberOfGap += nums[i] - nums[i-1] - 1
            i += 1
        print(numberOf0)
        print(numberOfGap)
        if numberOf0 >= numberOfGap:
            return True
        else:
            return False
            
print(Solution().isStraight([0,0,4,5,8]))
        