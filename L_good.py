class Fruit:
    # define something
    pass


class DryMethod(object):
    def dry(self):
        print("dry some thing")


class GreenGrape(Fruit, DryMethod):
    def dry(self):
        print("GreenGrape dry for cake")


class LitchiFruit(Fruit, DryMethod):
    def dry(self):
        print("Litchi dry is very great")


class Orange(Fruit):
    pass
