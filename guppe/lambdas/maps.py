"""
Map

Com Map, fazemos mapeamento de valores para funcao
"""

import math


def area(r):
    """Calcula a area de um circulo com raio 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma Comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map

# Map é uma funcao que recebe dois parametros, o primeiro é a funcao, o segundo um iteravel. Retorna um Map Object

areas = map(area, raios)

print("AREAS", areas)
print(type(areas))
print(list(areas))


# Forma 3 com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

print(list(map(lambda t: t * 4, raios)))

print(list(map(lambda k: k ** 4, (1, 2, 5, 6))))


"""
Mapeia a conversao de celsius para fahrenheit
"""
cidades = [("Changai", 17), ("Moscou", 10), ("Kiev", 15), ("Istambul", 14), ("Dubai", 16.5), ("Dubrovnik", 13.5),
           ("Montevidéu", 20), ("São Paulo", 23.5), ("Santiago", 18.5), ("Bogotá", 19.5), ("Nairóbi", 20.5), ("Porto Príncipe", 25.5)]

print(cidades)

c_para_f = lambda dado: (dado[0], round((9 / 5) * dado[1] + 32))
c_para_f2 = lambda dado: (dado[0], round(1.8 * dado[1] + 32))



print("------------")

print(list(map(c_para_f, cidades)))
print(list(map(c_para_f2, cidades)))
