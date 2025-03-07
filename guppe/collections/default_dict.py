"""
Modulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

#RECAP
dicionario = {'curso': 'Programacao em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])

print(dicionario['curso1'])

Default Dict -> Ao criar um dicionario utilizando-o, nos informamos um valor default,
podendo utilizar um lambda para isso. este valor sera utilizado sempre que nao houver um valor definido.
Caso tentemos acessar uma chave que nao existe, essa chave sera criada e o valor default sera atribuido


Default Dict nao retorna erro ao acessar uma chave inexistente, ele cria uma nova chave

Obs: Lambda sao funcoes sem nome que podem ou nao receber parametros de entrada e retornar valores.
"""
# fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 'Vai corinthians')

print(dicionario)

dicionario['curso'] = 'Programacao em Python: Essencial'

print(dicionario['outro'])
print(dicionario)
