"""@timer is a decorator for timing functions.

The decorated function will be run a selectable number of times
(default 100). During the timed runs, any output to stdout
is redirected to NUL. The minimum, average and longest run times are
printed to stdout, before running the function one final time.

When number of timed runs set to less than 2, the decorated function
will be timed running once only.

Any output to stdout during the final run will be printed normally.

Example Usage
-------------

    @timer()  # time 'myfunction' over 10 runs
    def myfunction(args):

    @timer(5)  # time 'myfunction' over 5 runs
    def myfunction(args):

    @timer(number=0)  # time a single run of 'myfunction'.
    def myfunction(args):


Parameters
----------
number : int
    The number of timed runs of the function.

"""

from functools import wraps
from time import time
from contextlib import redirect_stdout
from typing import Callable, Any

Func = Callable[..., Any]


def timer(number: int = 10) -> Func:
    """timeit type decorator"""
    def _decorator(func: Func) -> Func:
        @wraps(func)
        def _time_it(*args: Any | None, **kwargs: Any | None) -> None:
            if number > 1:
                with redirect_stdout(None):
                    times: list[float] = []
                    for _ in range(number):
                        start = time()
                        rslt = func(*args, **kwargs)
                        dur = time() - start
                        times += (dur,)
                print(f'> {func.__name__} {number} runs:  '
                      f'Min: {min(times):0.3e}   Average:'
                      f'{sum(times)/len(times):0.3e}   '
                      f'Max: {max(times):0.3e}')
                func(*args, **kwargs)
            else:
                start = time()
                rslt = func(*args, **kwargs)
                print(f'> {func.__name__} ran in '
                      f'{time() - start:0.3e} seconds.')
            return rslt
        return _time_it
    return _decorator
