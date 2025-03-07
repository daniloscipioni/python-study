"""
Modulo Collections: Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

# Em um dicionario a ordem de insercao dos elementos nao e garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')


OrderedDict ->  É um dicionario que nos garante a ordem de insercao dos elementos     


# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""

# Diferenca entre Dict e Ordered Dict


# Dicionarios comuns

from collections import OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True pq a ordem dos elementos nao importa para o dicionario

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False pq no OrderedDict importa a ordem
