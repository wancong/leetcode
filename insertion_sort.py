"""
a pure python implementation of the insertion sort algorithm
"""


def insertion_sort(coll):
    """insertion sort
    
    :type coll: collection
    :rtype: collection
    
    >>> insertion_sort([5, 1, 3, 2])
    [1, 2, 3, 5]
    >>> insertion_sort([])
    []
    >>> insertion_sort([1])
    [1]
    """
    for i in range(1, len(coll)):
        while i > 0 and coll[i - 1] > coll[i]:
            coll[i], coll[i-1] = coll[i-1], coll[i]
            i -= 1
    
    return coll

if __name__ == '__main__':
    user_input = input('numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))