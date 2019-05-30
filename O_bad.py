class Fruit:

    name = ""

    def __init__(self, name):
        self.name = name

    def pre_fruit(self):
        if self.name == "apple":
            print("wash")
        elif self.name == "orange":
            print("peel")

    def make_juice(self):
        if self.name == "apple":
            print("decorticate")
        if self.name == "orange":
            print("Juice the orange")
        pass

    pass


'it hard to add banana or other fruit to this class, that have to modifier 2 function pre_fruit and make_juice'

