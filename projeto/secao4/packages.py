from sys import path

import teste_packages.modulo
from teste_packages.modulo import sum1
from teste_packages import modulo
from teste_packages.modulo import *

print(sum1(1, 2))
print(teste_packages.modulo.sum1(1, 2))
print(modulo.sum1(1, 2))
print(variable, sum1(1, 2))
# print(path, sep='\n')
