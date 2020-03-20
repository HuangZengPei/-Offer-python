class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 
        target = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if target == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                target = nums[i]
                count = 1
        return target