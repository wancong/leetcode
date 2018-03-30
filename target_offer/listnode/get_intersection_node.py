""" Intersection of two linked lists
Write a program to find the node at which the intersection 
of two singly linked lists begins.
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def get_len(self, head):
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        return cnt
            
    def get_intersection_node(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        lenA = self.get_len(headA)
        lenB = self.get_len(headB)
        diff_len = 0
        
        if lenA > lenB:
            diff_len = lenA - lenB
            for _ in range(diff_len):
                headA = headA.next
        else:
            diff_len = lenB - lenA
            for _ in range(diff_len):
                headB = headB.next
                
        currA, currB = headA, headB
        while currA and currB:
            if currA == currB:
                return currA
            else:
                currA = currA.next
                currB = currB.next
                
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    node6.next = node7
    node7.next = node3
    
    ans_node = Solution().get_intersection_node(node1, node6)
    print(ans_node.val)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        