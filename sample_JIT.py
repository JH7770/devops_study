from functools import wraps
from time import time
import numba

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()

        print(f"func: {f.__name__}, args: [{args, kwargs}] took: {te-ts} sec")
    return wrap

@timing
@numba.jit(parallel=True)
def add_sum_threaded(rea):
    x, _ = rea.shape