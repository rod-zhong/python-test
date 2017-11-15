class User:
    name=""
    age=0
    def __init__(self, _age, _name):
        self.name = _name
        self.age = _age

    def toString(self):
        print("%s is %d old" %(self.name, self.age));
