""" 丑数
我们把只包含因子2、3和5的数称为丑数（Ugly Number）。
例如： 6、8是丑数，14不是，因为14还包含因子7。
1记作第一个丑数。
思路：
假设数组中已经有若干排好序的丑数，最大丑数是M。
下一个丑数必定是数组中某个数乘以2或3或5得到。
"""
def get_ugly_number(index):
    """Get n_th ugly number.
    
    :type index: int
    :rtype: int
    
    >>> get_ugly_number(10)
    12
    >>> get_ugly_number(1500)
    859963392
    >>> get_ugly_number(1)
    1
    """
    ugly_numbers = [0]*index
    ugly_numbers[0] = 1
    next_index = 1
      
    index2 = 0
    index3 = 0
    index5 = 0
    
    while next_index < index:
        min_value = min(ugly_numbers[index2]*2,
            ugly_numbers[index3]*3, 
            ugly_numbers[index5]*5)
        ugly_numbers[next_index] = min_value
              
        while ugly_numbers[index2]*2 <= ugly_numbers[next_index]:
            index2 += 1
        while ugly_numbers[index3]*3 <= ugly_numbers[next_index]:
            index3 += 1
        while ugly_numbers[index5]*5 <= ugly_numbers[next_index]:
            index5 += 1
        
        next_index += 1
  
    return ugly_numbers[-1]

print(get_ugly_number(10))
 












 