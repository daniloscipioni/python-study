def somar_numeros(*args):
    """
    Soma todos os numeros passados como argumento
    """
    return sum(args)


print(somar_numeros(1, 2, 3, 4, 56, 6))
print(somar_numeros(1, 1, 1, 1, 1, 1))
print(somar_numeros(1, 2, 3))
print(somar_numeros(10, 20, 30, 40))
print(somar_numeros())
