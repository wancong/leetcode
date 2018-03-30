"""Merge two stored linked list and return it as a new list.
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def merge_two_lists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        merged_list = ListNode(0)
        if l1.val < l2.val:
            merged_list = l1
            merged_list.next = self.merge_two_lists(l1.next, l2)
        else:
            merged_list = l2
            merged_list.next = self.merge_two_lists(l1, l2.next)
        return merged_list

if __name__ == "__main__":
    def list_to_ListNode(arr):
        dummy_root = ListNode(0)
        curr = dummy_root
        for number in arr:
            curr.next = ListNode(number)
            curr = curr.next
        return dummy_root.next
        
    l1 = list_to_ListNode([1, 2, 4])
    l2 = list_to_ListNode([1, 3, 4])
    
    node_new = Solution().merge_two_lists(l1, l2)
    curr = node_new
    while curr:
        print(curr.val, "->", end=" ")
        curr = curr.next