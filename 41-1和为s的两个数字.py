class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:return []
        p1 , p2 = 0 , len(nums) - 1
        while p1 < p2:
            if nums[p1] + nums[p2] == target:
                return [nums[p1], nums[p2]]
            elif nums[p1] + nums[p2] < target:
                p1 += 1
            else:
                p2 -= 1
        return []
        
test = Solution()
nums = [2,7,11,15]
print(test.twoSum(nums,3))