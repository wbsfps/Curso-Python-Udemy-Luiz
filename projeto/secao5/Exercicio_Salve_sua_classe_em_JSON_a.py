# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

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
    
    def __str__(self):
        return self.name

persons_list = []
path = "./projeto/secao5/"
path += f"persons.json"

def main():
    for i in range(2):
        name = input("Name: ")
        age = int(input("Age: "))

        person = Person(name, age)

        persons_list.append(vars(person))

    with open(path, "w", encoding="utf-8") as file:
            dump(persons_list, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()