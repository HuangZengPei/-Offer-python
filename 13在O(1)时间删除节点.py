class ListNode:
    def __init__(self):
        self.value = None
        self.next_node = None
        
class Solution:
    def delete_node(self,head_node,del_node):
        if not head_node and del_node:
            return False

        if del_node.next_node:             #删除的节点不是尾节点
            del_next = del_node.next_node
            del_node.value = del_next.value
            del_node.next_node = del_next.next_node
            del_next.value = None
            del_next.next_node = None
        
        elif del_node == head_node:
            del_node == None
            head_node == None
        else:
            node = head_node
            while node.next_node != del_node:
                node = node.next_node
            node.next_node = None
            del_node = None
        return head_node、