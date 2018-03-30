"""Reverse a singly linked list.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev, curr = None, head
    while curr:
        temp = curr
        curr = curr.next
        temp.next = prev
        prev = temp
    return prev
    
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    node_new = reverse_list(node1)
    curr = node_new
    while curr:
        print(curr.val, "->", end=" ")
        curr = curr.next
        
        
    
