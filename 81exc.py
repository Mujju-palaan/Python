class Person:
    def__init__(self, name, sex, age):
        self.name = name 
        self.sex = sex 
        self.age = age

    def__str__(self):
        return self.name + ' ' + self.sex + ' ' + str(self.age)
    def changeName(self, name):
        self.name = name
    def changeAge(self, age):
        self.age = age + 1

Person1 = Person('jane Dor','F',23)
Person2 = Person('Bob Smith','M',55)
print('Person 1: ' + str(Person1))
