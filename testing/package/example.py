from typing import Callable

def sum(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def testable_function(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    if a < b:
        raise ValueError("a cannot be less than b")
    return operation(a, b)

def not_covered():
    pass