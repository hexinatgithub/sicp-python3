def make_instance(cls):
    def get(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bound_method(value, instance)
    attributes = {}
    instance = {'get': get, 'set', set}
    return instance


def bound_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value


def make_class(attributes, base_cls=None):
    def get(name):
        if name in attributes:
            return attributes[name]
        elif base_cls is not None:
            return base_cls['get'](name)
    def set(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(cls, *args)
    cls = {'get': get, 'set': set, 'new': new}
    return cls

def init_instance(cls, *args):
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance