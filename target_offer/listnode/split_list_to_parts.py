""" Split Linked List in Parts
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]

Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): 
    def split_list_to_parts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        curr = root
        while curr:
            length += 1
            curr = curr.next
        len_mean = length // k
        len_over = length % k

        parts = []
        prev = ListNode(0)
        curr = root
        for _ in range(k):
            if curr:
                parts.append(curr)
                len_part = len_mean+1 if len_over > 0 else len_mean
                len_over -= 1
                for _ in range(len_part):
                    prev, curr = curr, curr.next
                prev.next = None
            else:
                parts.append(None)
        return parts
                
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    
    node1.next = node2
    node2.next = node3
    
    ans = Solution().split_list_to_parts(node1, 5)
    
    for new_node in ans:
        curr = new_node
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print('None')
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        