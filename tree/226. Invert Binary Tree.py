""" 226. Invert Binary Tree
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def invert_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        new_node = TreeNode(root.val)               
        new_node.left = self.invert_tree(root.right)
        new_node.right = self.invert_tree(root.left)
        
        return new_node 
        
if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(6)
    node7 = TreeNode(9)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    
    new_node = Solution().invert_tree(node1)

    def print_tree(t):
        if t: 
            print(t.val, end=" ")
        else:
            print("None", end=" ")
        if t.left: 
            print_tree(t.left)
        else:
            print("None", end=" ")
        if t.right: 
            print_tree(t.right)
        else:
            print("None", end=" ")
    print_tree(node1)  
    print('\n')
    print_tree(new_node)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    