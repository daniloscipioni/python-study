
from collections import defaultdict
entrada = [("fruta", "maçã"), ("fruta", "banana"), ("legume", "cenoura"),
           ("fruta", "laranja"), ("legume", "batata")]

saida = defaultdict(list)

for chave, valor in entrada:
    saida[chave].append(valor)

print(dict(saida))
