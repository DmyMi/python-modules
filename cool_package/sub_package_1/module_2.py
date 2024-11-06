# we can import packages from the same level of hiererchy using
# Be careful not to polute the current namespace
from ..sub_package_2 import module_3 as m3

def fun2():
    m3.fun3()
    print(f"{__name__}.fun2")