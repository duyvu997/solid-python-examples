"""
class IFruitProcess:
    def let_ferment(self):
        raise NotImplementedError

    def let_juice(self):
        raise NotImplementedError

    def let_use_normally(self):
        raise NotImplementedError


We can rewrite class IFruitProcess follow Interface Segregation Principle
"""


class IFruitProcess:
    def let_process_yourself(self):
        raise NotImplementedError


class Apple(IFruitProcess):
    def let_process_yourself(self):
        # we can implement what the apple can process.
        pass


class Orange(IFruitProcess):
    def let_process_yourself(self):
        # We can implement orange juice process in this method.
        pass
