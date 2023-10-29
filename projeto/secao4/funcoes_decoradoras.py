# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def create_function(func):

    def intern(*args, **kwargs):
        print('Vou te decorar')

        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        print(f'O seu resultado foi {result}')
        print('Ok, você foi decorado!')

        return result

    return intern


def string_reverse(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('O parâmetro deve ser uma string')


inverte_string_checando_parametro = create_function(string_reverse)
reverse = inverte_string_checando_parametro('123')

print(reverse)
