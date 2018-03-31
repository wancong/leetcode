""" 669. Trim a Binary Search Tree
Given a binary search tree and the lowest and highest boundaries as L and R, 
trim the tree so that all its elements lies in [L, R] (R >= L). 
You might need to change the root of the tree, 
so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
       
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def trim_BST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val > R:
            return self.trim_BST(root.left, L, R)
        if root.val < L:
            return self.trim_BST(root.right, L, R)
        
        root.left = self.trim_BST(root.left, L, R)
        root.right = self.trim_BST(root.right, L, R)
        
        return root
        
if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(0)
    node3 = TreeNode(4)
    node4 = TreeNode(2)
    node5 = TreeNode(1)
    
    node1.left = node2
    node1.right = node3
    node2.right = node4
    node4.left = node5
    
    new_root = Solution().trim_BST(node1, 1, 3)
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
    print_tree(new_root)    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        