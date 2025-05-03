# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f'{self.name} {self.surname}'

person = Person("William", "Santana")
print(person)
print(person.name)