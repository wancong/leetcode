"""两个链表的第一个公共节点
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def get_length(p_head):
    length = 0
    while p_head is not None:
        length += 1
        p_head = p_head.next
    return length
        
def find_first_common_node(p_head1, p_head2):
    """Find the first common node.
    
    :type p_head1: Node
    :type p_head2: Node
    :rtype: Node, common node, None if not found
    """
    length1 = get_length(p_head1)
    length2 = get_length(p_head2)
    diff_length = 0
    
    if length1 > length2:
        diff_length = length1 - length2
        p_long, p_short = p_head1, p_head2
    else:
        diff_length = length2 - length1
        p_long, p_short = p_head2, p_head1
        
    for i in range(diff_length):
        p_long = p_long.next
    
    while (p_long is not None 
        ) and (p_short is not None 
        ) and (p_long is not p_short):
        p_long = p_long.next
        p_short = p_short.next
        
    p_common = p_long
    return p_common
    
# test
if __name__ == '__main__':
    # 1 - 2 - 3 \
    #            6 - 7
    #     4 - 5 /
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node6
    node4.next = node5
    node5.next = node6
    node6.next = node7

    print('start...')
    p_common = find_first_common_node(node1, node4)
    if p_common is not None:
        print(p_common, p_common.value)
    else:
        print('not found')
    
    # 1 - 2 - 3 - 4 \
    #                7
    #         5 - 6 /
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node7
    node5.next = node6
    node6.next = node7

    print('start...')
    p_common = find_first_common_node(node1, node5)
    if p_common is not None:
        print(p_common, p_common.value)
    else:
        print('not found')
    
    # 1 - 2 - 3 - 4
    #           
    # 5 - 6 - 7
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node5.next = node6
    node6.next = node7

    print('start...')
    p_common = find_first_common_node(node1, node5)
    if p_common is not None:
        print(p_common, p_common.value)
    else:
        print('not found')





























