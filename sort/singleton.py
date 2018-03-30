class Singleton(object):
    """ Singleton mode. A class that has only one instance.
    
    >>> one = MyClass()
    >>> two = MyClass()
    >>> print(one is two)
    True
    >>> print(one == two)
    True
    >>> one.a = 3
    >>> two.a
    3
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1