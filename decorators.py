#---Intro to Decorators---
#function that wraps another function and changes or enhances the behavior
#has its own syntax @ sign you can do it without but you should use the @

#decorators can cause functions to lose metadata so use -from functools import wraps

#---Use Cases---
#speed test
from time import time
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
       t1 = time()
       result = fn(*args, **kwargs)
       t2 = time()
       print(f"Executing: {fn.__name__}")
       print(f"Time Elapsed: {t2-t1}")
       return print(result)
    return wrapper

@speed_test
def sum_nums_gen(nums):
    return sum(x for x in nums)

@speed_test
def sum_nums_list(nums):
    return sum([x for x in nums])

speed_test(sum_nums_gen(range(1,10000000)))
speed_test(sum_nums_list(range(1,10000000)))