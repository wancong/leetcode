"""delete duplicate node
exp: 1 1 2 3 3
1 2 3
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_duplicate(head):
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next # not duplicate of current node, move to next node
    return head
    
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    
    node1.next = node2   
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    new_head = delete_duplicate(node1)
    
    cur = new_head
    while cur:
        print(cur.val, "->", end=" ")
        cur = cur.next