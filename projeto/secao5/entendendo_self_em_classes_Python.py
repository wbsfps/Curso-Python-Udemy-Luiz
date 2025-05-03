# Entendendo self em classes Python.
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Car:
    def __init__(self, name: str,):
        self.name = name
    
    def accelerate(self):
        print(f'The {self.name} is accelerating...')

beetle = Car('Beetle')
Car.accelerate(beetle)
print(beetle.name)
beetle.accelerate()

celtic = Car('Celtic')
print(celtic.name)
celtic.accelerate()
Car.accelerate(celtic)