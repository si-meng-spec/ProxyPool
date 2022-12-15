def singleton(cls, *args, **kwargs):
    _instance = {}

    def inner(*__args, **__kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*__args, **__kwargs)
        return _instance[cls]

    return inner
