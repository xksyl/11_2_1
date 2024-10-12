import inspect

def introspection_info(obj):

    info = {}

    info['type'] = type(obj).__name__
    info['attributes'] = dir(obj)
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = inspect.getmodule(obj)
    info['module'] = module.__name__ if module else 'builtins'

    return info




number_info = introspection_info(42)
print(number_info)