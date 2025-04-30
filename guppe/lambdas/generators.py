"""
Generators

Tuple comprehension, não retorna uma tupla, retorna um generator object iterável.
A partir do primeiro uso ele é apagado da memória.

Quando um list/dict/set comprehension puderem ser escritos como um generator, o generator é preferível, pois
ocupa menos memória. Logo o generator é mais performático.


Exemplos


nomes = ["carlos", "carla", "camilla", "carina", "vanessa", "julius"]

print(all(nome[0] == "c" for nome in nomes))

res = (nome[0] == "c" for nome in nomes)

for re in res:
    print(re)

print(type(res))
"""

from sys import getsizeof

print(getsizeof("Geek"), getsizeof("Metallica"), getsizeof(120099083129083129381), getsizeof(True))


list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof(x * 10 for x in range(1000))

list_comp1 = [x * 10 for x in range(5)]
set_comp1 = {x * 10 for x in range(5)}
dict_comp1 = {x: x * 10 for x in range(5)}
gen1 = (x * 10 for x in range(5))

print("--------------")
print(list_comp1)
print(set_comp1)
print(dict_comp1)
print(gen1)
for val in gen1:
    print(val)
print("--------------")


print(f"Para fazer a mesma tarefa ocupamos em memoria\n"
      f"List comprehension: {list_comp} bytes \n"
      f"Set comprehension: {set_comp} bytes \n"
      f"Dict comprehension: {dict_comp} bytes \n"
      f"Generator expression: {gen} bytes")

gen = (x**2 for x in range(3))
for val in gen:
    print(val)  # 0, 1, 4


#range 0,1,2
for i in range(3):
    print(i)

#gen = (x * 10 for x in range(1000))
#for i in gen:
    #print(i)
"""
def contador():
    for i in range(3):
        yield i

gen = contador()

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

"""