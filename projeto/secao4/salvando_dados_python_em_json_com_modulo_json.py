import json

person = {
    'name': 'William',
    'surname': 'Santana',
    'address': [
        {'street': 'S1', 'number': 123},
        {'street': 'S2', 'number': 456},
    ],
    'height': 1.74,
    'favorite_numbers': (2,3,4,5,6),
    'dev': True,
    'nothing': None
}

path = './projeto/secao4/'
path += 'salvando_dados_python_em_json_com_modulo_json.json'
with open(path, 'w', encoding='utf-8') as file:
    json.dump(person, file, indent=2, ensure_ascii=False)


with open(path, 'r', encoding='utf-8') as file:
    person = json.load(file)
    print(person)
    print(type(person))