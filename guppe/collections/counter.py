"""
Módulo Collections - Counter
https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um iteravel como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário
, contendo como chave o elemento da lista passada como paramentro e como valor a quantidade de ocorrencias desse elemento



# utilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1, 1, 1, 2, 34, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 34: 2, 45: 2, 66: 2, 43: 1})
print(res)

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

from collections import Counter

texto = """Gorgosaurus (que significa "lagarto feroz") foi um gênero de dinossauro terópode
tiranossaurídeo que viveu durante o Cretáceo Superior, estágio Campaniano, entre 76,6 e 75,1 milhões de anos.
Restos fósseis foram encontrados na província canadense de Alberta e no estado estadunidense de Montana. 
Os paleontólogos reconhecem apenas a espécie-tipo, Gorgosaurus libratus, embora outras espécies 
tenham sido erroneamente referidas ao gênero."""

palavras = texto.split()

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrências
print(res.most_common(5))
