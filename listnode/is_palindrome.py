""" Palindrome Linked List
1-2-3-2-1
Could you do it in O(n) time and O(1) space?

快慢指针，当快指针到达尾部时，慢指针刚好指向中间
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def is_palindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
        
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    print(Solution().is_palindrome(node1))
            
            
            
            
            
            
            
            
            
            
            
            