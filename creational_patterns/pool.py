# encoding=utf-8

"""
    @author: anzz
    @date: 2019/3/29
    @doc：
        池模式，当频繁的创建销毁相同的对象时，我们需要把他们维护在内存池中，这样以减少频繁创建
    对象的开销。常使用在创建数据库连接池，线程池等。示例中通过queue对象管理对象，运用上下文协议
    __enter__ 和 __exit__ 实现对池中的对象获取和放回操作。
"""
import queue


class ObjectPool(object):
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    # 初始化queue用于存放不同的对象
    sample_queue = queue.Queue()
    # 放入实例对象
    sample_queue.put('yam')
    # 获取到queue中的对象
    with ObjectPool(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    # 退出时又放回了queue中，所以可以再次获取。
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('sam')
    if not sample_queue.empty():
        print(sample_queue.qsize())


if __name__ == '__main__':
    main()