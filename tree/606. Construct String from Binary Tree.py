""" 606. Construct String from Binary Tree
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def tree_to_string(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        
        if root is None: return ""
        s = ""
        s += str(root.val) 
        if not root.left and not root.right: return s
        s += '(' + self.tree_to_string(root.left) + ')'
        s += '(' + self.tree_to_string(root.right) + ')'
        return s
        
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    
    print(Solution().tree_to_string(node1))
 

        
        
        
    