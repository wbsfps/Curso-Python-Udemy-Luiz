# Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def action(self):
        print(f"The {self.name} is performing an action")
    def eating(self, eat: str):
        return f"{self.name} is eating a {eat}"
    
    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)

lion = Animal("Lion")
print(lion.name)
lion.action()
print(lion.eating("meat"))
print(lion.execute("banana"))