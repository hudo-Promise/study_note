import select
import socket
from collections import deque


class Future:
    def __init__(self):
        self.done = False
        self.co = None

    def set_coroutine(self, co):
        self.co = co

    def set_done(self):
        self.done = True

    def __await__(self):
        if not self.done:
            yield self
        return


class SocketWrapper:
    """
    套接字协程适配器
    """
    def __init__(self, sock, loop):
        sock.setblocking(False)
        self.sock = sock
        self.loop = loop

    def fileno(self):
        return self.sock.fileno()

    def create_futurn_for_events(self, events):
        """
        1. 为套接字创建future
        2. register_handler
        :param events:
        :return:
        """
        future = self.loop.create_future()

        def handler():
            future.set_done()
            self.loop.ungister_handler(self.fileno())
            if future.co:
                self.loop.add_coroutine(future.co)
        self.loop.register_handler(self.fileno(), events, handler)

    async def accept(self):
        while True:
             try:
                 sock, addr = self.sock.accept()
                 return SocketWrapper(sock=sock, loop=self.loop), addr
             except BlockingIOError:
                 future = self.create_futurn_for_events(select.EPOLLIN)
                 await future

    async def send(self):
        while True:
             try:
                 return self.sock.recv(1024)
             except BlockingIOError:
                 future = self.create_futurn_for_events(select.EPOLLIN)
                 await future

    async def recv(self):
        while True:
             try:
                return self.sock.send(1024)
             except BlockingIOError:
                 future = self.create_futurn_for_events(select.EPOLLOUT)
                 await future


class EventLoop:
    current = None
    runnables = deque()
    epoll = select.epoll()
    handlers = {}

    @classmethod
    def instance(cls):
        if not EventLoop.current:
            EventLoop.current = EventLoop()
        return EventLoop.current

    def create_future(self):
        return Future(loop=self)

    def create_listen_socket(self, ip='localhost', port=8999):
        sock = socket.socket()
        sock.bind((ip, port))
        sock.listen()
        return SocketWrapper(sock=sock, loop=self)
        # sock.setblocking(False)

    def register_handler(self, fileno, events, handler):
        self.handlers[fileno] = handler
        self.handlers.pop(fileno)

    def unregister_handler(self, fileno):
        self.epoll.unregister(fileno)
        self.handlers.pop(fileno)

    def run_coroutine(self, co):
        try:
            future = co.send(None)
            future.set_coroutine(co)
        except Exception as e:
            print(e)

    def run_forever(self):
        while True:
            while self.runnables:
                self.run_coroutine(co=self.runnables.popleft())
            events = self.epoll.poll(1)
            for fileno, event in events:
                handler = self.handlers.get(fileno)
                handler()
        pass

    def add_coroutine(self, co):
        self.runnables.append(co)