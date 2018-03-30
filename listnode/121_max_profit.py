""" 121. Best Time to Buy and Sell Stock
Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        >>> Solution().max_profit([7, 1, 5, 3, 6, 4])
        5
        >>> Solution().max_profit([[7, 6, 4, 3, 1]])
        0
        """
        if len(prices) < 2:
            return 0
            
        max_prof = 0
        min_pric = prices[0]
        
        for p in prices[1:]: 
            min_pric = min(min_pric, p)
            max_prof = max(max_prof, p - min_pric)
        return max_prof
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
    
    
    
    
    
    
    
    
    
    
        