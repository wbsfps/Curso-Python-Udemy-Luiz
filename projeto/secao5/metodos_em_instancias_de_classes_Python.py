# Métodos em instâncias de classes Python

class Car:
    def __init__(self, name: str,):
        self.name = name
    
    def accelerate(self):
        print(f'The {self.name} is accelerating...')

beetle = Car('Beetle')
print(beetle.name)
beetle.accelerate()

celtic = Car('Celtic')
print(celtic.name)
celtic.accelerate()