# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # 双堆栈
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:return None
        stackA = []
        stackB = []
        while headA:
            stackA.append(headA)
            headA = headA.next
            
        while headB:
            stackB.append(headB)
            headB = headB.next
            
        res = None
        while stackA and stackB:
            nodea = stackA.pop()
            nodeb = stackB.pop()
            if nodea == nodeb:
                res = nodea
                if not stackA or not stackB:   # 有一个为空，说明走到头结点
                    return res
            else:
                return nodea.next
                
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:return None
        lengthA,lengthB = 0,0
        while headA:
            lengthA += 1
            headA = headA.next
            
        while headB:
            lengthB += 1
            headB = headB.next
        
        if lengthA < lengthB:
            diff = lengthB - lengthA
            indexA = 0
            while indexA < diff:
                headA = headA.next
                indexA += 1
        elif lengthA > lengthB:
            diff = lengthA - lengthB
            indexB = 0
            while indexB < diff:
                headB = headB.next
                indexB += 1
                
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
        
        