import heapq
class Solution(object):
    # 堆排序
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not arr or k > len(arr) or k == 0:return []
        # python中是小根堆，因此先取相反数
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k,len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp,-arr[i])
        ans = [-x for x in hp]
        return ans
        
    # 快排的思想
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not arr or k > len(arr) or k <= 0:return []
        start , end = 0 , len(arr)-1
        index = self.partition(arr,start,end)
        while index != k-1:
            if index < k-1:
                start = index + 1
                index = self.partition(arr,start,end)
            else:
                end = index - 1
                index = self.partition(arr,start,end)
        ans = arr[:k]
        return ans
        
    def partition(self,arr,start,end):
        pivot = arr[start]
        while start < end:
            while start < end and pivot <= arr[end]:
                end -= 1
            arr[start] = arr[end]
            while start < end and arr[start] < pivot:
                start += 1
            arr[end] = arr[start]
        arr[start] = pivot
        return start