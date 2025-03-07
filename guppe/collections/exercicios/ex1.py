lista: list[int] = []
while len(lista) < 6:
    valor: int = int(input("Digite um numero: "))
    lista.append(valor)

for valor in lista:
    print(valor)
