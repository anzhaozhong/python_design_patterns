# encoding=utf-8

"""
    @author: anzz
    @date: 2019/3/29
    @doc:
        建造者模式，比如说我们要创建一个mysql节点。apt install mysql-client就好了，但是底层中
    他会先去寻找资源，下载，解析，调用。最后给我们一个可用的mysql-client。这个就是构建的过程。
"""


class Build(object):
    floor = None
    size = None

    def __init__(self, floor='one', size=1):
        # 构建函数的过程中，进行拆分，多个对象被创建。此过程封装在build的构造函数中，
        # 解藕了构建过程，对外提供一个简单的调用
        self.build_floor(floor)
        self.build_size(size)

    def build_floor(self, floor):
        # 解藕后的实例化
        self.floor = str(floor)

    def build_size(self, size):
        self.size = int(size)

    def __str__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


if __name__ == '__main__':
    building = Build('two', 10)
    print(building)
