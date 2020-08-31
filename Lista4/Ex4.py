import math
from collections import defaultdict
from inspect import getfullargspec


class overload:
    functions = defaultdict(dict)

    def __init__(self, func):
        self.functions = overload.functions[func.__name__]
        no_args = len(getfullargspec(func).args)
        self.functions[no_args] = func

    def __call__(self, *args, **kwargs):
        return self.functions[len(args)](*args, **kwargs)


@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


if __name__ == '__main__':
    print(norm(2, 4))
    print(norm(2, 3, 4))
