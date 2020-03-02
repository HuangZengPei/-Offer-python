class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:return False
        row = len(array)
        column = len(array[0])
        i,j = 0,column-1
        while i< row and j>=0:  #右上角的数
            if array[i][j] < target:
                i += 1
            elif array[i][j] > target:
                j -= 1
            else:return True
        return False