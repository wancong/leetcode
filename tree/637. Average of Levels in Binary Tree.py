""" 637. Average of Levels in Binary Tree
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3, 
on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def average_levels(self, root):
        """ depth_first_search
        :type root: TreeNode
        :rtype: List[float]
        """
        node_info = []
        def dfs(node, depth=0):
            if node:
                if len(node_info) <= depth:
                    node_info.append([0, 0])  # inital
                node_info[depth][0] += node.val
                node_info[depth][1] += 1
                
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        
        dfs(root)
        return [float(sum)/cnt for sum, cnt in node_info]
        
    def average_levels_1(self, root):
        """ breadth_first_search
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None: return []
        average = []
        queue = [root]
        while queue:
            level_sum, level_cnt = 0, len(queue)
            for _ in range(level_cnt):
                node = queue.pop(0)
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            average.append(level_sum*1.0 / level_cnt)
        return average
            
        
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
       
    print(Solution().average_levels(node1))
    print(Solution().average_levels_1(node1))


    
