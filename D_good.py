from abc import ABCMeta, abstractmethod


class IFruitProcess(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def exe_method(self):
        pass


class Wash(IFruitProcess):
    def exe_method(self):
        print("Wash the fruit with water ")


class Ferment(IFruitProcess):
    def exe_method(self):
        print("# Some thing can ferment")


class Apple(object):
    process_method = IFruitProcess

    def set_method(self, input_method):
        assert isinstance(input_method, IFruitProcess)
        self.process_method = input_method

    def exe_process(self):
        self.process_method.exe_method()


def main():
    apple = Apple()
    wash_method = Wash()
    apple.set_method(wash_method)  # <<- injection here
    apple.exe_process()
