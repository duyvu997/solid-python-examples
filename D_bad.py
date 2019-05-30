
class FruitProcess:
    way_process = ''

    def __init__(self, method):
        self.way_process = method

    def set_method_wash(self):
        print("some fruit can be wash")


class Apple:
    process_method = FruitProcess

    def __init__(self):
        self.process_method = FruitProcess('wash')  # by default

    def process_adv(self):
        self.process_method.set_method_wash()


"""
when we change method_process apple from 'wash' to 'ferment' we have change the Apple implement
"""