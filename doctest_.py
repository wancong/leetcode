def abc(x):
    '''
    >>> abc(1)
    2
    >>> abc(0)
    1
    '''
    return x + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
