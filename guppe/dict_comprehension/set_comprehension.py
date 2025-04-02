"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro Exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)


# OBS: Faca uma alteracao na estrutura acima para gerar um dicionario ao inves de um set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para finalizar (Consjunto nao aceita valores repetidos e nem respeita ordenacao)

letras = {letra for letra in 'Geek University'}

print(letras)
