class Solution(object):
    def getFirstK(self,nums,target,start,end):
        if start > end:return -1
        middle = int((start + end )/2)
        if nums[middle] <target:
            start = middle + 1
        elif nums[middle] > target:
            end = middle -1
        else:
            if (middle > 0 and nums[middle-1] !=target) or middle == 0:
                return middle
            else:
                end = middle -1
        return self.getFirstK(nums,target,start,end)
            
    def getLastK(self,nums,target,start,end):
        if start > end:return -1
        middle = int((start + end )/2)
        if nums[middle] <target:
            start = middle + 1
        elif nums[middle] > target:
            end = middle -1
        else:
            if (middle < end and nums[middle+1] != target) or middle==end:
                return middle
            else:
                start = middle + 1
        return self.getLastK(nums,target,start,end)
            
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return 0
        number = 0
        first = self.getFirstK(nums,target,0,len(nums)-1)
        last = self.getLastK(nums,target,0,len(nums)-1)
        if first > -1 and last > -1:
            number = last-first+1
        return number
        
test = Solution()
nums = [1]
print(test.search(nums,1))