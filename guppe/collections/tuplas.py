"""
As tuplas são imutáveis
"""

tupla = (1, 2, 3, 4, 5, 6)
print(tupla)

print(type(tupla))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))


tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

# Tuplas são definidas pelas virgulas e não pelo uso do parênteses
tupla4 = (4,)  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# Desempacotamento de tupla

tupla = ("Geek University", "Programação em Python: Essencial")

escola, curso = tupla
print(escola)
print(curso)

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis


# concatenação de tuplas
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

tupla2 = (7, 8, 9, 10)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobrescrever seus valores

print(tupla1)


# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)


# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ("a", "b", "c", "c", "e", "a", "b")
print(tupla.count("c"))


# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1 - Meses do ano

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla
print(meses.index("Fevereiro", 0))

# slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.
# * Isso porque trabalhar com elementos imutáveis traz segurança para o código.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)


# Somando tuplas
tupla_sum = (1, 3, 3, 6, 7)
print(sum(tupla_sum))
print(max(tupla_sum))
print(min(tupla_sum))
