"""
a pure python implementation of the quick sort algorithm in place
1 inital check point: n[0]
  leftmark：n[1]
  rightmark: n[-1]
  
2 leftmark go and check one by one, x < n[0]
  rihgtmark go and check one by one, x > n[0]
  when both stop, swap
  when leftmark > rightmark, n[0] get its place, swap 

3 recursively sublist

"""

def m_quick_sort(coll):
    """quick sort in place
    
    :type coll: collection
    :rtype: collection
    
    >>> m_quick_sort([3, 2, 1, 4])
    [1, 2, 3, 4]
    >>> m_quick_sort([1])
    [1]
    >>> m_quick_sort([])
    []
    >>> m_quick_sort([-2, -1, -3])
    [-3, -2, -1]
    """      
    _quick_sort(coll,0,len(coll)-1)
    return coll
    
def _quick_sort(coll, left, right):
    if left < right:
        point = partition(coll, left, right)
        _quick_sort(coll, left, point-1)
        _quick_sort(coll, point+1, right)
    return None
    
def partition(coll, left, right):
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