import importlib

import recarregando_modulos_2


print(recarregando_modulos_2.variable)

for i in range(10):
    print(i)
    importlib.reload(recarregando_modulos_2)

print('fim')
