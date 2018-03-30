class Singleton(object):
    """singleton by __new__
    
    >>> one = MyClass()
    >>> two = MyClass()
    >>> one is two
    True
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1