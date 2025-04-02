"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programacao possuem uma estritura de dados chamadas de arrays
    - Unidimensionais (Arrays / Vetores)
    - Multidimensionais (Matrizes)

Em Python existe Listas

numeros = [1, 'a', True, 2, 3, 4, 5]




# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

print(listas)
print(type(listas))


# Como fazemos para acessar os dados

print(listas[0][1])  # Acesso ao numero 2

print(listas[2][1])  # Acesso ao numero 8
print(listas[2][-2])  # Acesso ao numero 8

# Iterando com loops em uma lista aninhada
for lista in listas:
    for numero in lista:
        print(numero)


print("-------")
# List Comprehension
[[print(valor) for valor in lista] for lista in listas]
"""

# Outros exemplos

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores inicias

print([['*' for i in range(1, 4)] for j in range(1, 4)])
