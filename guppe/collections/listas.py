"""
As tuplas são mutáveis
"""


print(type([]))


lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ["G", "e", "e", "k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"]

lista3 = []

lista4 = list(range(11))

lista5 = list("Geek University")

lista6 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]


if 8 in lista4:
    print("Encontrei o número 8")
else:
    print("Não encontrei o número 8")

print(lista6)
lista6.sort()
print(lista5.count("e"))
print(lista6)
# insere 1 elemento no final lista
lista6.append(8)
print(lista6)
# insere mais de um elemento na lista
lista6.extend([1, 2, 3, 233])
print(lista6)
# insert insere na posição desejada
lista6.insert(2, 4)
print(lista6)

# Sao a mesma coisa
lista7 = lista6 + lista5
lista6.extend(lista5)
print(lista6)
print(lista7)

# reverte a lista
lista7.reverse()
print(lista7)

print(lista7[::-1])

# copia a lista
lista8 = lista4.copy()
print(lista8)


# remove o ultimo elemento da lista e pop retorna o elemento removido
test = lista8.pop()
print(f"O elemento removido foi {test}")
print(lista8)

print(lista7)
# remove o elemento pelo indice
test2 = lista7.pop(2)
print(f"O elemento removido foi {test2}")
print(lista7)

# limpa a lista
lista7.clear()
print(lista7)


# Repete elementos na lista
lista_1 = [1, 2, 3]
print(lista_1)
lista_1 = lista_1 * 3

print(lista_1)

# Convertendo string para lista

curso = "Programacao Python Essencial"
print(curso)
curso = curso.split()
print(curso)

curso = "Programacao,Python,Essencial"
print(curso)
curso = curso.split(sep=",")
print(curso)

# Convertendo lista para string
lista_string = ["Programacao", "Python", "Essencial"]
print(lista_string)

# coloca - entre os elementos da lista
curso = '-'.join(lista_string)
print(curso)
# coloca espaço entre os elementos da lista
curso = ' '.join(lista_string)
print(curso)

cores = ["amarelo", "azul", "vermelho", "branco"]

print(cores[-1])  # branco
print(cores[-2])  # vermelho

cores = list(enumerate(cores))

print(cores)
cores_1 = ["amarelo", "azul", "vermelho", "branco", "vermelho"]
# Retorna o primeiro elemento da lista na sequencia
print(cores_1.index("vermelho"))  # 2

# Retorna o primeiro elemento da lista na sequencia a partir do indice 3
print(cores_1.index("vermelho", 3))  # 2

print(cores_1[1:2])
print(cores_1[0:-3])


# com parametro passo, comeca no indice 0 e vai ate o indice 3 pulando de 2 em 2
print(cores_1[0::2])

print(cores_1[1::-2])  # azul
print(cores_1[::-2])  # vermelho, vermelho, azul

cores_1.reverse()
print(cores_1)


lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformar lista em tupla

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# desempactoamento de lista

lista = [1, 2, 3]

# Se houver mais elementos na lista que variaveis, vai dar erro
num1, num2, num3 = lista
print(num1, num2, num3)


# Copiando listas (shallow e deep copy)
# Deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)

print(nova)

# Ao utilizar lista.copy foram criadas duas listas independentes com o mesmo conteudo (deep copy)

# Shallow copy
print("---------")
lista = [1, 2, 3]

print(lista)

nova = lista

print(nova)

nova.append(4)

print(lista)

print(nova)
