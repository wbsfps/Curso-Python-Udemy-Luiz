from Exercicio_Salve_sua_classe_em_JSON_a import Person, path, main
from json import load

with open(path, "r") as file:
    persons = load(file)
    
    p1 = Person(**persons[0])
    p2 = Person(**persons[1])
    print(p1.name, p1.age)
    print(p2.name, p2.age)