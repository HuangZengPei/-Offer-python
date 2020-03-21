import functools
class Solution(object):
    def compare(s1,s2):
        if s1 + s2 < s2 + s1:
            return -1
        elif s1 + s2 > s2 + s1:
            return 1
        else:
            return 0
            
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:return ''
        nums = [str(num) for num in nums]
        nums = sorted(nums, key=functools.cmp_to_key(compare))
        return ''.join(nums)