class IFruitProcess:
    def let_ferment(self):
        raise NotImplementedError

    def let_juice(self):
        raise NotImplementedError

    def let_use_normally(self):
        raise NotImplementedError


"""
This interface process fruit. class Apple or Orange must implement all method in interface
"""


class Apple(IFruitProcess):
    def let_ferment(self):
        pass

    def let_juice(self):
        pass

    def let_use_normally(self):
        pass


class Orange(IFruitProcess):
    def let_ferment(self):
        pass

    def let_juice(self):
        pass

    def let_use_normally(self):
        pass


"""
But class Orange not necessary implement method let_ferment. it never use. Or if we add new method in class 
IFruitProcess, all sub-class of IFruitProcess must implement or an error will be thrown.  
"""