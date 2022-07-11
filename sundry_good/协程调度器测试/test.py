import random
import string
import time

from loop import coroutine, YieldLoop

# 求等差数列之和
# @coroutine
# def test1():
#     sum = 0
#     for i in range(1, 11):
#         if i % 2 == 1:
#             sum += yield i
#     print('sum = ', sum)
#
#
# YieldLoop.instance().add_coroutine(test1())
# YieldLoop.instance().run_until_complete()

# 生产者消费者模型
from collections import deque


@coroutine
def producer(q):
    while True:
        good = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        q.append(good)
        cnt = len(q)
        print("product good, cnt=", cnt)
        if cnt > 0:
            yield


@coroutine
def consumer(q):
    while True:
        while len(q) <= 0:
            yield
        good = q.popleft()
        print('consumer get good = {}, cnt = {}'.format(good, len(q)))
        time.sleep(1)


q = deque()
YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(consumer(q))
YieldLoop.instance().run_until_complete()
