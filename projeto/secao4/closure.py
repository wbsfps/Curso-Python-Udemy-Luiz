"""
Closure e funções que retornam outras funções
"""


def create_salutation(salutation):
    def saudar(name):
        return f'{salutation}, {name}!'
    return saudar


speak_bom_dia = create_salutation('Bom dia')
speak_boa_noite = create_salutation('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(speak_bom_dia(nome))
    print(speak_boa_noite(nome))
