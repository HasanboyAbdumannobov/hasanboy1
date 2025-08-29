class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("Ali", 20)
p2 = Person("Vali", 19)
print(p1 > p2)
