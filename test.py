class Person:
    # def __init__(self, name):
    #     print(f"class name: {name}")
    #     self.name = name

    def getName(self, name):
        print(f"Method name: {name}")
        # print(f"self name {self.name}")
        self.name = name
        return self.name


if __name__ == "__main__":
    print(f"name {__name__}")
    p = Person()
    print(p.getName("simbu"))
