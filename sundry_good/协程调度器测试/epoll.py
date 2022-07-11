# io多路复用TCPServer模型  -- 单线程支持多并发
import socket
import select

def serve():
    server = socket.socket()
    server.bind(('127.0.0.1', 8999))
    server.listen()

    epoll = select.epoll()
    epoll.register(server.fileno(), select.EPOLLIN)
    contents = {}
    connections = {}
    while True:
        # 通过epoll系统调用 监听可读fds
        events = epoll.poll(10)
        for fileno, event in events:
            # 新连接

            if fileno == server.fileno():
                s, addr = server.accept()
                print('new connection from addr ', addr)
                epoll.register(s.fileno(), select.EPOLLIN)
                connections[s.fileno()] = s
            elif event == select.EPOLLIN:
                s = connections[fileno]
                content = s.recv(1024)
                # 关闭连接
                if not content:
                    epoll.unregister(fileno)
                    s.close()
                    connections.pop(fileno)
                else:
                    content = content.upper()
                    # 改为关注写事件
                    epoll.modify(fileno, select.EPOLLOUT)
                    contents[fileno] = content
            # 写事件就绪
            elif event == select.EPOLLOUT:
                try:
                    content = contents[fileno]
                    s = connections[fileno]
                    s.send(content)
                    # 改为关注读事件
                    epoll.modify(fileno, select.EPOLLIN)
                except:
                    epoll.unregister(fileno)
                    s.close()
                    connections.pop(fileno)
                    contents.pop(fileno)

    pass
