"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.
- Aqui no Python, os conjuntos são chamados de Sets.
- Da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados; 

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}.

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;




# Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.
print(s)  # O set não aceita valores duplicados, então ele vai eliminar os valores repetidos.

print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)

print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que, além de não termos valores duplicados, nao temos ordem


# Listas aceitam valores duplicados - mantem a mesma ordem
lista = [99, 2, 34, 23, 2, 12, 1, 44, 34, 5]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados - mantem a mesma ordem
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 34, 5
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicados - mantem a mesma ordem
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados - gera a propria ordem
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 34, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

for valor in s:
    print(valor)


# Usos interessantes com sets
# converte lista para set
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
           'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

print(len(set(cidades)))


# Adicionando elementos e um conjunto

s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade nao gera erro
print(s)

# Removendo elementos e um conjunto
s = {1, 2, 3}

# Forma 1

s.remove(3)  # Nao é indice pois conjuntos nao sao indexados, nenhum valor é retornado
print(s)
# Caso o valor nao seja encontrado, sera gerado um keyError

# Forma 2

s.discard(22)  # Se valor nao for encontrado, nenhum erro é gerado
print(s)

# Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

# Forma 1 - Deep copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)  # manteve o mesmo valor depois da alteracao de "novo"

# Forma 3 - Shallow copy
novo = s  # as duas variaveis terao o mesmo valor
print(novo)

novo.add(4)

print(novo)
print(s)  # valor é alterado


# Podemos remover todos os itens do conjunto
s = {1, 2, 3}
s.clear()
print(s)


# Métodos matemáticos

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}


# Nomes unicos

# Forma 1 - com union - Recomendado
unicos1 = estudantes_java.union(estudantes_python)
unicos2 = estudantes_python.union(estudantes_java)

# {'Gustavo', 'Julia', 'Patricia', 'Fernando', 'Pedro', 'Guilherme', 'Ana', 'Ellen', 'Marcos'}
print(unicos1)
print(unicos2)

# Forma 2 - com |
unicos3 = estudantes_java | estudantes_python
print(unicos3)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Nomes que estao em ambos os cursos
# Forma 1 - intersection
# {'Patricia', 'Julia'}
ambos = estudantes_python.intersection(estudantes_java)
print(ambos)

# Forma 2 - &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Estudantes que nao estao no outro curso
# {'Marcos', 'Ellen', 'Pedro', 'Guilherme'}
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
