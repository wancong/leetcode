"""
a pure python implementation of the quick sort algorithm
"""

def quick_sort(coll):
    """ quick sort
    1 任选一个节点
    2 小的都换节点前面，大的节点后面
    3 合并
    
    >>> quick_sort([3, 2, 1, 4])
    [1, 2, 3, 4]
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    >>> quick_sort([3, 2, 1])
    [1, 2, 3]
    """
    less = []
    equal = []
    greater = []
    if len(coll) > 1:
        for x in coll:
            if x < coll[0]:
                less.append(x)
            elif x == coll[0]:
                equal.append(x)
            else:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return coll