# python design patterns
设计模式是为实际开发中遇到的问题所服务的。尽量结合问题，考虑场景的使用设计模式，才是正确的。

> 阅读[英文版设计模式](https://github.com/faif/python-patterns) 再结合实际工作中的使用，
进一步思考 **why**,**when**,**where**。

#### 构造者模式
| 模式 | 简单描述 |
|:-------:| ----------- |
| [工厂模式](creational_patterns/factory_method.py)| 委托一个专门的函数/方法来创建实例
| [抽象工厂模式](creational_patterns/abstract_factory.py)|生产具有相同方法的实例
| [博格模式](creational_patterns/borg.py)|实例中具有共享状态的单例
| [建造者模式](creational_patterns/builder.py)|替代多个构造函数,构建器对象接收参数并返回构造对象
| [懒加载模式](creational_patterns/lazy_evaluation.py) | 用到时再实例化
| [池模式](creational_patterns/pool.py) | 提前实例化，并维护一定数量相同类型的对象
| [原型模式](creational_patterns/prototype.py) | 
