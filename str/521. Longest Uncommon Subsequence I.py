""" 521. Longest Uncommon Subsequence I
Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 
"""
class Solution(object):
    def longest_uncommon(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        
        >>> Solution().longest_uncommon('aba', 'cdc')
        3
        """
        if a ==b: return -1
        else: return max(len(a), len(b))
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
        
        