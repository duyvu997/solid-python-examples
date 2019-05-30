
class Fruit:

    def pre_fruit(self):
        pass

    def make_juice(self):
        pass


class Tools:
    def pre_tools(self):
        pass

    def clean_tools(self):
        pass


class MakeFruitJuice (Fruit, Tools):
    pass
