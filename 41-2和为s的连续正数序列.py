class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        if target <= 0:return []
        small,middle,big = 1, int((1+target)/2), 2
        result = []
        sum = 0
        while small < middle:
            for i in range(small,middle+1):
                sum += i
                if sum == target:
                    result.append(self.getList(small,i))
                    sum = 0
                    break
                elif sum>target:
                    sum = 0
                    break
            small += 1
            sum = 0
        return result
        
    # 剑指offer版本,减少运算
    def offer_findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        if target <= 0:return []
        if target < 3:return []
        small,middle,big = 1,int((1+target)/2),2
        result = []
        cursum = small + big
        while small < middle:
            if cursum == target:
                result.append(self.getList(small,big))
            while cursum > target and small < middle:
                cursum -= small
                small += 1
                if cursum == target:
                    result.append(self.getList(small,big))
            big += 1
            cursum += big
        return result
                
    def getList(self,small,big):
        list = []
        while small <= big:
            list.append(small)
            small += 1
        return list
        