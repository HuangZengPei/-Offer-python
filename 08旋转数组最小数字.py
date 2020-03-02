# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:return None
        p1 , p2 = 0, len(rotateArray)-1
        indexMid = p1
        while rotateArray[p1] >= rotateArray[p2]:
            if p2 - p1 == 1:
                indexMid = p2
                break
            indexMid = int((p1 + p2) /2)
            if rotateArray[p1] == rotateArray[indexMid] and rotateArray[indexMid] == rotateArray[p2]:   # 当三个数相同，只能顺序查找
                return self.minOrder(rotateArray,p1,p2)
            if rotateArray[indexMid] >= rotateArray[p1]:
                p1 = indexMid
            elif rotateArray[indexMid] <= rotateArray[p2]:
                p2 = indexMid
        return rotateArray[indexMid]
        
    def minOrder(self, numbers, index1, index2):
        result = index1
        for i in range(index1+1, index2+1):
            if numbers[i] < result:
                result = numbers[i]
        return result
        
        
test = Solution()
numbers = [1,0,1,1,1]
print(test.minNumberInRotateArray(numbers))