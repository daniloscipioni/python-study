from collections import OrderedDict

entrada = {"a": 3, "b": 1, "c": 2}
crescente = {}
decrescente = {}
ordered = OrderedDict(entrada)

for w in sorted(entrada, key=entrada.get, reverse=False):
    crescente[w] = entrada[w]

for w in sorted(entrada, key=entrada.get, reverse=True):
    decrescente[w] = entrada[w]

print(f'Entrada {entrada}')
print(f'Crescente {crescente}')
print(f'Decrescente {decrescente}')
