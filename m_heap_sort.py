"""
a pure python implementation of the heap sort algorithm
"""

def m_heap_sort(arr):
    """heap sort
    
    :type arr: array
    :rtype: array
    
    >>> m_heap_sort([3, 2, 1, 4, 5])
    [1, 2, 3, 4, 5]
    >>> m_heap_sort([])
    []
    >>> m_heap_sort([1])
    [1]
    """
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    """get max heap
    
    :type arr: array
    :type n: int, length
    :type i: index, subtree root
    :rtype: None
    
    """
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    