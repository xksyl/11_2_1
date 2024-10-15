import inspect

def introspection_info(obj):

    info = {}

    info['type'] = type(obj).__name__
    info['attributes and methods'] = dir(obj)
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info ['methods'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    module = inspect.getmodule(obj)
    info['module'] = module.__name__ if module else 'builtins'

    return info




number_info = introspection_info(42)
print(number_info)
