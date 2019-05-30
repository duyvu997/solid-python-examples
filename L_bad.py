import abc


class Fruit(abc.ABC):
    def dry(self):
        print("dry some thing")


class GreenGrape(Fruit):
    def dry(self):
        print("GreenGrape dry for cake")


class LitchiFruit(Fruit):
    def dry(self):
        print("Litchi dry is very great")


"But orange shouldn't dry"


class Orange(Fruit):
    def dry(self):
        raise Exception



