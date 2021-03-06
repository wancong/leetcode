""" 617. Merge Two Binary Trees
Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that 
if two nodes overlap, then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):        
    def merge_trees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode  
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.merge_trees(t1.left, t2.left)
            root.right = self.merge_trees(t1.right, t2.right)
            return root
        else:
            return t1 or t2
        
if __name__ == "__main__":
    node11 = TreeNode(1)
    node12 = TreeNode(3)
    node13 = TreeNode(2)
    node14 = TreeNode(5)
    
    node11.left = node12
    node11.right = node13
    node12.left = node14
    
    node21 = TreeNode(2)
    node22 = TreeNode(1)
    node23 = TreeNode(3)
    node24 = TreeNode(4)
    node25 = TreeNode(7)
    
    node21.left = node22
    node21.right = node23
    node22.right = node24
    node23.right = node25
    
    new_node = Solution().merge_trees(node11, node21)
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
    print_tree(new_node)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        