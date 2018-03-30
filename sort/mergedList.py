class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	#循环 l1,l2被改变
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        """
        ans = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next  = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return ans.next
	
	#循环 l1,l2不变
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        """
		import copy
        l1_, l2_ = copy.deepcopy(l1), copy.deepcopy(l2)
        ans = cur = ListNode(0)
        while l1_ and l2_:
            if l1_.val < l2_.val:
                cur.next = l1_
                l1_ = l1_.next
            else:
                cur.next = l2_
                l2_ = l2_.next
            cur = cur.next
        cur.next = l1_ or l2_ 
        return ans.next
	