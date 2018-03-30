"""
a pure python implementation of the selection sort algorithm
"""

def selection_sort(coll):
    """selection sort
    
    :type coll: collection
    :rtype: collection
    
    >>> selection_sort([2, 1, 3, -1])
    [-1, 1, 2, 3]
    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    """
    length = len(coll)
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if coll[j] < coll[min]:
                min = j
        coll[i], coll[min] = coll[min], coll[i]

    return coll

if __name__ == '__main__':
    user_input = input('numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(selection_sort(unsorted))