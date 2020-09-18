class Command(object):
    func_dict = {}
    class_dict = {}


command_base = Command()


def command_class(cls):
    command_base.class_dict[cls.__name__] = cls()
    
    def func():
        return cls
    
    return func


def command_func(func):
    command_base.func_dict[func.__name__] = func
    
    def _func():
        return func
    
    return _func
