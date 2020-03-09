# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here  打乱排序
        if not array:return
        p1 ,p2 = 0, len(array)-1
        while p1 < p2:
            if array[p1] &0x1 == 0 and array[p2] &0x1 == 1:
                array[p1],array[p2] = array[p2],array[p1]
                p1 += 1
                p2 -= 1
            elif array[p1] &0x1 == 1:
                p1 += 1
            elif array[p2] &0x1 == 0:
                p2 -= 1
                
    def reOrderArray(self, array):
        # write code here  不打乱顺序
        if not array:return
        p1 ,p2,array_len = 0,0, len(array)
        while p1 < array_len and p2 < array_len:
            if array[p1] &0x1 == 1:       # p1为奇数
                p1 += 1
            else:
                p2 = p1 + 1
                while p2 < array_len and array[p2] &0x1 == 0:
                    p2 += 1 
                if p2 >= array_len:return array
                #p2为奇数，需要更换位置
                temp = array[p2]
                self.moveArray(array,p1,p2)  # 将p1到p2的数往后移一位
                array[p1] = temp
        return array
        
    def moveArray(self,array,start,end):
        array_len = len(array)
        if start > array_len or end > array_len:return
        if end <= start:return
        while end >= start:
            array[end] = array[end-1]
            end -= 1
            
                    
test = Solution()
array = [1,2,3,4,5,6,7]
test.reOrderArray(array)
print(array)