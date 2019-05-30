class Fruit:
    name = ""

    def pre_fruit(self):
        pass

    def make_juice(self):
        pass


class Apple(Fruit):
    color = ""

    def pre_fruit(self):
        pass

    def make_juice(self):
        pass


class Orange(Fruit):

    taste = ""

    def pre_fruit(self):
        pass
    # do some thing with orange

    def make_juice(self):
        pass


'to add new fruit is easy, don\'t need modifier parent class  '


class Banana(Fruit):

    weight = ""

    def pre_fruit(self):
        pass

    def make_juice(self):
        pass
