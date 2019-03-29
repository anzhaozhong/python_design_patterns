# encoding=utf-8

"""
    @author: anzz
    @date: 2019/3/29
    @doc:
        懒加载模式，顾名思义，需要用到这个实例时再去加载。减少不必要的开销，延迟实例化的时间。
    django框架源码中的settings就是一个懒加载模式。
    https://github.com/django/django/blob/ffd18732f3ee9e6f0374aff9ccf350d85187fac2/django/utils/functional.py#L19
    示例里用了类装饰器和函数装饰器两种方法来实现懒加载模式。
    类装饰器模式是利用描述符__get__特性来实现，
    函数装饰器是通过 builtin 装饰器 property 来实现。
"""

import functools


class LazyProperty(object):
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    # 描述符内置函数，当类成员是一个对象实例化时，会调用此方法。
    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    # 由property装饰，就可以像调用普通属性一样调用，内部还有setter、deleter方法。
    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @LazyProperty
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    Jhon = Person('Jhon', 'Coder')
    print("Name: {0}    Occupation: {1}".format(Jhon.name, Jhon.occupation))
    print("加载之前`dict`:", end='')
    print(Jhon.__dict__)
    print("Jhon's relatives: {0}".format(Jhon.relatives))
    print("加载之后`dict`:", end='')
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.__dict__)
    print(Jhon.parents)
    print(Jhon.call_count2)


if __name__ == '__main__':
    main()
