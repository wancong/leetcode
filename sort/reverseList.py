# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
		
		Input: 1->2->3
		Output: 3->2->1
        """
        prev, curr = None, head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        return prev