### 协程
* 意义
    * 
* 实现方式
    * greenlet
    ```python
    # pip install greenlet
    from greenlet import greenlet
    def func1():
        print(1)  # 输出 1
        gr2.switch()  # 切换到func2 函数
        print(2)  # 输出 2
        gr2.switch()  # 切换到 func2 函数 从上一次执行的位置继续向后执行


    def  func2():
        print(3)  # 输出3 
        gr1.switch() # 切换到func1函数 从上一次执行的位置继续向后执行
        print(4)  # 输出 4

    gr1.greenlet(func1)
    gr2.greenlet(func2)

    gr1.switch()  # 第一步  执行func1函数
    ```
    * yield
    ```python
    def func1():
        yield 1
        yield from func2()
        yield 2

    def func2():
        yield 3
        yield 4
    
    f1 = func1()
    from item in f1:
        print(item)
    ```
    * asyncio
    ```python
    # v > 3.4
    import asyncio

    @asyncio.coroutine
    def func1():
        print(1)
        yield from asyncio.sleep(2)
        print(2)
    
     @asyncio.coroutine
    def func2():
        print(3)
        yield from asyncio.sleep(2)
        print(4)
    
    tasks = [
        asyncio.ensure_future(func1()),
        asyncio.ensure_future(func2())
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    ```
    * async await
    ```python
    # v > 3.5
    import asyncio

    async def func1():
        print(1)
        await from asyncio.sleep(2)
        print(2)
    
    async def func2():
        print(3)
        await from asyncio.sleep(2)
        print(4)
    
    tasks = [
        asyncio.ensure_future(func1()),
        asyncio.ensure_future(func2())
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    ```

* 事件循环
    * 死循环 -- 检测并执行代码
        ```python
        # 生成一个事件循环
        loop = asyncio.get_event_loop()
        loop.run_until_complete()
        # 将任务放到任务列表

        # 以上代码可被简化
        asyncio.run()
        ```

* await 关键字
    * await +  可等待对象
        * 协程对象 : 协程函数实例化
        * Future对象 : 
        * Task对象 : task继承future对象  

* 迭代器
    * 内部实现了iter next 方法的对象  就是迭代器
    * 异步迭代器 ： 内部实现了aiter anext 方法的对象
* 可迭代对象
    * 通过iter方法返回的迭代器
    * 异步可迭代对象 ： 通过aiter方法返回的迭代器
* 上下文管理器
    * 实现了enter 和 exit 方法的对象
* 异步上下文管理器
    * 实现了aenter 和 aexit 方法的对象
* uvloop
    * asyncio事件循环的替代方案
    ```python
    import asyncio
    import uvloop
    asyncio.set_event_loop_policy(unloop.EventLoopPolicy())
    ```
* 案例
    * 异步redis
    ```python
    import asyncio
    import aioredis

    async def exrcute(address, password):
        redis = await aioredis.creat_redis(address, password)
        await redis.hmset_dict()
        await redis.hgetall()
        redis.close()
        await redis.wait_closed()

    ```
    * 异步mysql
    ```python
    import asyncio
    import aiomysql

    async def exrcute():
        conn = await aiomysql.connect()
        curr = await conn.cursor()
        await curr.execute()
        result = await curr.fetchall()
        await curr.close()
        conn.close()
    ```
    * FastAPI 框架
    ```python
    import asyncio
    import uvicorn
    from fastapi import FastAPI
    app = FastAPI()

    @app.get("/")
    def index():
        # 普通接口
        pass

    @app.get("/red")
    async def red():
        # 异步接口
    ```