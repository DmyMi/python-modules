import os


def get_path(filename):
    """This is a sample doc string"""
    head, tail = os.path.split(filename)
    breakpoint()
    return head


filename = __file__
print(f'path = {get_path(filename)}')