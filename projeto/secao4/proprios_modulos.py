# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import modularizacao_m
from modularizacao_m import module_variable, sum1

# print('Este nome se chama', __name__)

print(modularizacao_m.module_variable)
print(module_variable)
print(sum1(1, 2))
print(modularizacao_m.sum1(1, 2))
print(modularizacao_m.sum_teste(1, 2))
