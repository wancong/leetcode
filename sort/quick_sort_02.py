"""quick sort inplace
1 选中arr[0], 小的扔前面，大的扔后面
2 一次遍历，就可以确定arr[0]最后的位置
3 递归剩下的两部分
"""
def quick_sort(arr):
    """quick sort inplace
    
    :type arr: list
    :rtype: list
    
    >>> quick_sort([3, 2, 1, 4])
    [1, 2, 3, 4]
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    """
    def partition(arr, left, right):
        pivot_value = arr[left]
        left_point = left + 1
        right_point = right
        
        done = False
        while not done:
            while arr[left_point] <= pivot_value:
                left_point += 1
            while arr[right_point] > pivot_value:
                right_point -= 1
            if left_point > right_point:
                done = True
            else:
                arr[left_point], arr[right_point] = arr[right_point], arr[left_point]
        arr[left], arr[right_point] = arr[right_point], arr[left]
        return right_point
        
    def _quick_sort(arr, left, right):
        if left < right:
            point = partition(arr, left, right)
            _quick_sort(arr, left, point-1)
            _quick_sort(arr, point+1, right)
        
    _quick_sort(arr, 0, len(arr)-1)
    return arr

    
    
    
    
    
    
    pivot_value = coll[left]
    left_point = left + 1
    right_point = right
    
    done = False
    while not done:
        while coll[left_point] <= pivot_value:
            left_point += 1
        while coll[right_point] > pivot_value:
            right_point -= 1
        if left_point > right_point:
            done = True
        else:
            coll[left_point], coll[right_point] = coll[right_point], coll[left_point]
    
    coll[left], coll[right_point] = coll[right_point], coll[left]
    return right_point    
