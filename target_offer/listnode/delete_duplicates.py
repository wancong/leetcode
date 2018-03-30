"""Remove duplicates from sorted list
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def delete_duplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

if __name__ == "__main__":
    def list_to_ListNode(arr):
        dummy_root = ListNode(0)
        curr = dummy_root
        for number in arr:
            curr.next = ListNode(number)
            curr = curr.next
        return dummy_root.next
        
    arr = []
    node_new = Solution().list_to_ListNode(arr)
    curr = node_new
    while curr:
        print(curr.val, "->", end=" ")
        curr = curr.next