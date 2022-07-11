"""
装饰器的使用
decorator

"""
import time
import functools  # 消除装饰器对函数的副作用


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call {}, call time = {}'.format(func.__name__, int(time.time())))
        return func()
    return wrapper


@log
def func():
    print("hello world, hello function...")


func()

