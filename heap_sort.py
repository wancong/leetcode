"""
a pure python implementation of the heap sort algorithm

通过max heap，每次找出数组中最大的元素
1 从下到上，调整max heap
2 根节点是当前数组的最大元素，根节点移动到末尾（根节点和末尾叶子节点对调）
3 最大的一个确定了，数组规模减小了1，重复上述步骤，直到只剩1个元素
"""
def heap_sort(coll):
    """heap sort
    
    :type coll: collection
    :rtype: collection
    
    >>> heap_sort([3, 2, 1, 4, 0])
    [0, 1, 2, 3, 4]
    >>> heap_sort([1])
    [1]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -1, -3])
    [-3, -2, -1]
    """
    n = len(coll)
    # n//2 - 1: root i, left 2*i + 1, right 2*i + 2
    for i in range(n//2 - 1, -1, -1):
        heapify(coll, n, i)
    for i in range(n-1, 0, -1):
        coll[i], coll[0] = coll[0], coll[i]
        heapify(coll, i, 0)
    return coll

def heapify(coll, n, i):
    """get a max heap
    :type coll: collection
    "type n": int, length
    "type i": int, root of subheap
    "rtype": None
    """
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and coll[left] > coll[largest]:
        largest = left
    if right < n and coll[right] > coll[largest]:
        largest = right
    
    if largest != i:
        coll[largest], coll[i] = coll[i], coll[largest]
        heapify(coll, n, largest)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        