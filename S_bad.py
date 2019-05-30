class MakeFruitJuice:
    name = ""

    def __init__(self, name):
        self.name = name

    def pre_fruit(self):
        print("prepare " + self.name)

    def pre_tools(self):
        tool_name = "default"
        return tool_name

    def make_juice(self):
        pass

    def clean_tools(self, tool_name):
        print("clean" + tool_name)


'When you have new fruit  --> you must rewrite code.'
'When you change the tool or upgrade tools, you also rewrite '


def main():
    mfj = MakeFruitJuice("orange")
    print(mfj)
