"""
celery 是一个基于python实现的异步任务调度工具  也是一个任务队列
发送 短信验证  激活邮件

服务端
消息中间件 broker(可以定义多个) 不提供队列  使用第三方 MQ redis
任务执行  worker(可以定义多个)  定时取任务
任务结果存储(非必须)

客户端 发起任务


使用   在客户端初始化celery
celery_app = Celery()
通过装饰器的方式@celery.app_task
func.delay() 发起任务
"""

"""
redis 持久化
快照 RDB 默认持久化方式
    save 900 1
    redis fork函数把主进程复制一个子进程  子进程把内存数据遍历出来
    存放到配置文件指定的二进制文件dump.rdb中
    使用简单 读写快   容易造成数据丢失
AOF 以日志文件的方式追加

"""
