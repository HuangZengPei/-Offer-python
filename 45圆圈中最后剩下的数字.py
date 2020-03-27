class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        josep = list(range(n))
        index = 0
        while josep:
            temp = josep.pop(0)         # 弹出第一个，如果是第n个就删除，不是添加到末尾
            index += 1
            if index == m:
                index = 0
                if len(josep) == 1:
                    return josep[0]
                continue
            josep.append(temp)
            if len(josep) == 1:
                return josep[0]
                
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return -1
        last = 0
        for i in range(2,n+1):
            last = (last + m) % i
        return last
                
print(Solution().lastRemaining(70866,116922))