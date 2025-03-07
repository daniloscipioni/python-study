
lista: list[int] = []
contador_par = 0
while len(lista) < 10:
    valor = int(input("Digite um numero: "))
    lista.append(valor)

    if valor % 2 == 0:
        contador_par = contador_par + 1


print(lista)
print(f'Ha {contador_par} pares na lista')
