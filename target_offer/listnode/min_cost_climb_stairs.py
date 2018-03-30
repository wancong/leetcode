""" 746. Min Cost Climbing Stairs
Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""
class Solution(object):
    def min_cost_climb_stairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        
        >>> Solution().min_cost_climb_stairs([10, 15, 20])
        15
        >>> Solution().min_cost_climb_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        6
        """
        cost_a = cost[0]
        cost_b = cost[1]
        for c in cost[2:]:
            cost_a, cost_b = cost_b, min(cost_a, cost_b) + c
        return min(cost_a, cost_b)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)        
        