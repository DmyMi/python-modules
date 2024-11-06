# the __all__ attribute will be honored when somebody executes
# from my_module import *
# it will import only what you specify in the __all__ list
__all__ = ['some_function']

def some_function() -> str:
    return "Hello module!"

def other_function() -> str:
    return "Not imported with *"