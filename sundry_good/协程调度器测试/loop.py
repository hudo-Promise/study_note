from collections import deque
from wrapper import CoroutineWrapper


import inspect
import functools


class YieldLoop:
    current = None
    runnables = deque()

    # 单例模式
    @classmethod
    def instance(cls):
        if not YieldLoop.current:
            YieldLoop.current = YieldLoop()
        return YieldLoop.current

    def add_runnables(self, coro):
        self.runnables.append(coro)

    def add_coroutine(self, coro):
        """ 添加协程到调度器
        """
        # 对类型进行判断
        assert isinstance(coro, CoroutineWrapper), 'isinstance(coro) != CoroutineWrapper'
        self.runnables.append(coro)

    def run_coroutine(self, coro):
        """ 执行协程
        """
        try:
            coro.send(coro.context)
        except StopIteration as e:
            pass

    def run_until_complete(self):
        while YieldLoop.runnables:
            coro = YieldLoop.runnables.popleft()
            self.run_coroutine(coro)


# 协程装饰器
def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        if inspect.isgenerator(gen):
            coro = CoroutineWrapper(YieldLoop.instance(), gen)
            return coro
        else:
            raise RuntimeError('[Coroutinewrapper] error type({}) is not supported'.format(type(gen)))
    return wrapper
