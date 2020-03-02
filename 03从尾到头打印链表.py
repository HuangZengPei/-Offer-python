class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:return []
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        return stack[::-1]