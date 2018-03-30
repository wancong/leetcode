"""quick sort
1 任选一个元素a
2 小的放前，大的放后，一次遍历后，a的位置确定
3 小的部分和大的部分，两个子序列，递归
"""
def quick_sort(arr):
    """quick sort
    
    >>> quick_sort([3, 2, 1, 4])
    [1, 2, 3, 4]
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    """
    if len(arr) <= 1:
        return arr
        
    less = []
    equal = []
    greater = []
    
    for i in arr:
        if i < arr[0]:
            less.append(i)
        if i == arr[0]:
            equal.append(i)
        if i > arr[0]:
            greater.append(i)

    return quick_sort(less) + equal + quick_sort(greater)