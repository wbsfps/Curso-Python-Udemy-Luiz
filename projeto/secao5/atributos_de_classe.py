# Atributos de classe.
from datetime import datetime

class Person:
    attribute = "value"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def set_age(self, age: int):
        self.age = age
        return
    def get_age(self):
        return self.age
    
    def get_year_of_birth(self):
        return datetime.now().year - self.age

person = Person("Bob", 20)
print(Person.attribute)
print(person.get_age())
print(person.get_year_of_birth())
person.set_age(22)
print(person.get_age())
print(person.get_year_of_birth())
