class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
        print("-doesn't run")

    def do_sth(self):
        print(self.name, self.age, "is eating")


class Engineer(People):
    pass


class SoftEngineer(People):
    def __init__(self, name, age):
        People.__init__(self, name, age)
        self.skill = 'Python'


rod = Engineer("Rod", 34)
rod.do_sth()
zzt = SoftEngineer("Rod", 34)
zzt.do_sth()
