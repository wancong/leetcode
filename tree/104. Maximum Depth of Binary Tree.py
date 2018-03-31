""" 104. Maximum Depth of Binary Tree
For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        m_depth = [0]
        def dfs(node, depth=0):
            if node: depth += 1
            m_depth[0] = max(m_depth[0], depth)
            if node.left: dfs(node.left, depth)
            if node.right: dfs(node.right, depth)
        dfs(root)
        return m_depth[0]
        
    def max_depth_1(self, root):
        if root is None: return 0
        return max(self.max_depth_1(root.left), self.max_depth_1(root.right)) + 1
        
if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    
    print(Solution().max_depth(node1))
    print(Solution().max_depth_1(node1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    