# encoding=utf-8

"""
    @author: anzz
    @date: 2019/3/28
    @doc:
        众多实例共享数据，因为需要创建不同的对象，而不是只创建一个对象，所以这里不使用单例模式。
    使用场景，比如创建数据库链接池时,由于所有对象保持一致状态，修改一个即可。
"""


class Borg(object):

    # 类属性，实例共享
    __shared_state = {}

    def __init__(self):
        # 实例属性和类属性绑定，所有实例属性相同
        self.__dict__ = self.__shared_state
        self.state = 'init'

    def __str__(self):
        return self.state


class SubBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    # 不同的实例对象，但是属性相同
    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = SubBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))