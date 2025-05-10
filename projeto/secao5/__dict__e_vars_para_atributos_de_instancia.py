# __dict__ e vars para atributos de instância
from datetime import datetime
from json import dump

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

data = {'name': 'Bob', 'age': 20}
person = Person(**data)
print(person.__dict__.get('name'))
print(vars(person))

path = "./projeto/secao5/"
path += "__dict__e_vars_para_atributos_de_instancia.json"

with open(path, "w+", encoding="utf-8") as file:
    dump(data, file, indent=2, ensure_ascii=False)
