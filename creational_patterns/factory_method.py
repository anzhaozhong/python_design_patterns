# encoding=utf-8

"""
    @author: anzz
    @date: 2019/3/29
    @doc:
        工厂模式，根据传入参数返回确定的实例对象。不同条件下创建不同实例时使用
"""


class DogCrow(object):
    def __init__(self):
        print("wangwangwang")


class CatCrow(object):
    def __init__(self):
        print("miaomiaomiao")


# 这个工厂函数封装了内部构建实例的过程和选择逻辑
def crow(animal):
    if animal.lower() == "cat":
        return CatCrow()
    elif animal.lower() == "dog":
        return DogCrow()
    else:
        # 如果处理不了，抛出异常
        raise Exception("neither dog or cat")


if __name__ == '__main__':
    animal_params = str(input("请输入:cat / dog"))
    crow(animal_params)
