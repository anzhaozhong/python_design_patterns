# encoding=utf-8

"""
    @author: anzz
    @date: 2019/3/28
    @doc：
        在java中，抽象工厂函数提供一个获取对象的接口，而不必直接指定实际的类对象。
    在python中，我们可以通过callable这个函数来实现。每个类都继承一个__callable__方法，
    代表这个对象可以调用。
"""

import random
from abc import ABCMeta, abstractmethod


class PetShop(object):

    """对外暴露的接口类"""

    def __init__(self, animal_factory=None):
        """这里根据传入的参数，选择实例化的对象，为了简化，这里直接传入类"""

        self.pet_factory = animal_factory

    def show_pet(self):
        """调用对象方法"""

        # 实例化对象
        pet = self.pet_factory()

        # 调用对象的一些方法或者返回对象
        print("可爱的 {}".format(pet))
        print("它在 {}".format(pet.speak()))


class AbstractAnimal(metaclass=ABCMeta):
    """抽象类，供子类继承，实现抽象方法"""

    @abstractmethod
    def speak(self):
        """子类必须实现的方法"""
        pass


class Dog(AbstractAnimal):

    """工厂函数封装的对象，不对外暴露，由工厂函数进行实例化。"""

    def speak(self):
        return "汪汪汪"

    def __str__(self):
        return "狗"


class Cat(AbstractAnimal):

    def speak(self):
        return "喵喵喵"

    def __str__(self):
        return "猫"


def random_animal():
    """动态传入参数"""
    return random.choice([Dog, Cat])()


if __name__ == "__main__":
    # AbstractAnimal()
    # 第一种方式，直接传入参数
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("")

    # 工厂传入一个func
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print("=" * 20)
