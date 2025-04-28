"""
Any e All

all(): retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

Exemplos

"""
print("ALL")
print(all([0, 1, 2, 3, 4]), all([1, 2, 3, 4]), all({}),all("Geek University"))  # Retorna False True True True pois  o all[0]   == False

nomes = ["carlos", "cristiano", "castro", "cassiano", "carina", "camilla"]

print(all([nome[0] == "c" for nome in nomes]))

# caso em que o iterável é vazio, e considerado como True pelo all
print(all([letra for letra in "klmnop" if letra in "abcdefghij"]))

print(all([num for num in range(0, 100) if num  == 0]),all([num for num in range(50, 100) if num % 2 != 0]))

"""
any(): retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna falso

Exemplos
"""

print("ANY")
print(any([0, 1, 2, 3, 4]), any([1, 2, 3, 4]), any({}),any("Geek University"))

nomes = ["carlos", "cristiano", "castro", "cassiano", "carina", "camilla"]

print(any([nome[0] == "c" for nome in nomes]))

print(any([num for num in range(2, 25, 2) if num % 2 == 17]))
"""
"""