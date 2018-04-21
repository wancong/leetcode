"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2list(self, root, arr):
        """ tree to list, mid search
        :type root: TreeNode
        :type arr: list
        :rtype: None
        """
        if root is None: return
        self.tree2list(root.left, arr)
        arr.append(root.val)
        self.tree2list(root.right, arr)
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        arr = []
        self.tree2list(root, arr)
        left, right = 0, len(arr)-1
        while left < right:
            sum_val = arr[left] + arr[right]
            if sum_val == k:
                return True
            elif sum_val < k:
                left += 1
            else:
                right -= 1
        return False
        
if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    
    print(Solution().findTarget(node1, 9))
    
    
    
    
    