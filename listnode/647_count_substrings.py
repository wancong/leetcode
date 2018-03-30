""" 647. Palindromic Substrings
Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
class Solution(object):
    def __init__(self):
        self.cnt = 0
        
    def count_substrings(self, s):
        """
        :type s: str
        :rtype: int
        
        >>> Solution().count_substrings("abc")
        3
        >>> Solution().count_substrings("aaa")
        6
        """
        if s is None: return 0

        length = len(s)
        def _check_pali(s, left, right):
            """ Count plindromic at index a
            :type s: str
            :type left: index
            :type right: index
            """
            while left>=0 and right<length and s[left] == s[right]:
                self.cnt += 1
                left -= 1
                right += 1

        for i in range(length):
            _check_pali(s, i, i)
            _check_pali(s, i, i+1)
        
        return self.cnt
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
 
 
 
 
 
 
 
            
        