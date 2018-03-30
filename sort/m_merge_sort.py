def merge_sort(coll):
    """
    >>> merge_sort([3, 2, 1, 4])
    [1, 2, 3, 4]
    >>> merge_sort([])
    []
    >>> merge_sort([0, 0, 1, -1, 5])
    [-1, 0, 0, 1, 5]
    """
    if len(coll) > 1:
        midpoint = len(coll) // 2
        
        left = merge_sort(coll[:midpoint])
        right = merge_sort(coll[midpoint:])
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                coll[k] = left[i]
                i += 1
            else:
                coll[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            coll[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            coll[k] = right[j]
            j += 1
            k += 1
    return coll        