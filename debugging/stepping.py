import os

def get_path(filename):
    head, tail = os.path.split(filename)
    return head

filename = __file__
breakpoint()
filename_path = get_path(filename)
print(f'path = {filename_path}')