"""
a pure python implementation of the merge sort algorithm
"""

def merge_sort(coll):
    """merge sort
    1 n序列分为n/2两个子序列
    2 子序列采用并归排序
    3 排好序的子序列合为一个序列
    
    :type coll: collection
    :rtype: collection
    
    >>> merge_sort([2, 3, 1])
    [1, 2, 3]
    >>> merge_sort([])
    []
    >>> merge_sort([1])
    [1]
    """ 
    length = len(coll)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(coll[:midpoint])
        right_half = merge_sort(coll[midpoint:])
        i = j = k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                coll[k] = left_half[i]
                i += 1
            else:
                coll[k] = right_half[j]
                j += 1
            k += 1
            
        while i < left_length:
            coll[k] = left_half[i]
            i += 1
            k += 1
            
        while j < right_length:
            coll[k] = right_half[j]
            j += 1
            k += 1
        
    return coll

if __name__ == '__main__':
    user_input = input('numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))      