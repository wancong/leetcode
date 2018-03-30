"""
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
        
def delete_duplicate_node(p_head):
    if p_head is None:
        return
        
    p_pre_node = None
    p_node = p_head  # 封存p_head，防止丢失
    while p_node is not None:
        p_next = p_node.next
        if p_next is not None and p_next.value == p_node.value:
            value = p_node.value
            p_to_be_delete = p_node
            
            while p_to_be_delete is not None and p_to_be_delete.value == value:
                p_next = p_to_be_delete.next
                p_to_be_delete = p_to_be_delete.next
            
            if p_pre_node is None:  # 要删除的是头节点
                p_head = p_next
            else:
                p_pre_node.next = p_next
            
            p_node = p_next
        else:
            p_pre_node = p_node
            p_node = p_node.next          

    return p_head
    
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
                
    node_new = delete_duplicate_node(node1)
    
    node_tmp = node_new
    while node_tmp is not None:
        print(node_tmp.value)
        node_tmp = node_tmp.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    