"""
bubble sort algorithm

python3 -m doctest -v bubble_sort.py

python bubble_sort.py
"""

def bubble_sort(coll):
    """bubble sort algorithm in Python
    
    :type coll: collection
    :rtype: collection
    
    >>> bubble_sort([1, 3, 2])
    [1, 2, 3]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-5, -1])
    [-5, -1]
    """
    length = len(coll)
    for i in range(length):
        for j in range(length-1):
            if coll[j] > coll[j+1]:
                coll[j], coll[j+1] = coll[j+1], coll[j]
    
    return coll

if __name__ == '__main__':
    user_input = input('numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))    
    