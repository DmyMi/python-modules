import os

def get_path(fname):
    breakpoint()
    head, tail = os.path.split(fname)
    for char in tail:
        pass  # Check filename char
    return head

filename = __file__
filename_path = get_path(filename)
print(f'path = {filename_path}')