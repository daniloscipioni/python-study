"""
List Comprehension

- Utilizando List Comprehension nos podemos gerar novas listas com dados processados a partir de outro iteravel

# Sintaxe da List Comprehension

[ dado for dado in iteravel]


# Exemplo

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

Para endtender melhor o que esta acontecendo devemos dividir a expressao em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10




res = [numero / 2 for numero in numeros]

print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)


# List Comprehensions versos Loop

# Loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehensions
print([numero * 2 for numero in numeros])
numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros_dobrados)
"""

# Outros exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])


# 2

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.capitalize() for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
