# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row = len(matrix)
        column = len(matrix[0])
        result = []
        if not matrix or row <= 0 or column <=0:
            return result
        start = 0
        while column > start*2 and row > start*2:
            self.printMatrixInCircle(matrix,column,row,start,result)
            start += 1
        return result
    
    def printMatrixInCircle(self,matrix,column,row,start,result):
        endX = column-1-start
        endY = row-1-start
        
        for i in range(start,endX+1):
            number = matrix[start][i]
            result.append(number)
        
        # 从上到下打印一列
        if start < endY:
            for i in range(start+1,endY+1):
                result.append(matrix[i][endX])
                
        if start< endX and start < endY:
            for i in range(endX-1,start-1,-1):
                result.append(matrix[endY][i])
                
        if start<endX and start < endY-1:
            for i in range(endY-1, start,-1):
                result.append(matrix[i][start])
                
test = Solution()
numbers = [[1]]
res = test.printMatrix(numbers)
print(res)