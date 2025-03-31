from enum import Enum


class Operador(Enum):
    SUM = "soma"
    SUB = "subtracao"
    MULT = "multiplicacao"
    DIV = "divisao"


def calculadora(operador, *args):
    """
    Realiza uma operacao matematica nos numeros fornecidos com base no operador
    """

    if (operador == Operador.SUM.value):
        return sum(args)
    elif (operador == Operador.SUB.value):
        result = args[0]
        for arg in args[1:]:
            result = result - arg
        return result
    elif (operador == Operador.MULT.value):
        result = 1
        for arg in args:
            result = result * arg
        return result
    elif (operador == Operador.DIV.value):
        result = args[0]
        for arg in args[1:]:
            result = result / arg
        return int(result)


print(calculadora("soma", 1, 2, 3, 4))          # Deve retornar 10
print(calculadora("multiplicacao", 2, 3, 4))    # Deve retornar 24
print(calculadora("subtracao", 10, 5, 1))       # Deve retornar 4
print(calculadora("divisao", 20, 2, 2))         # Deve retornar 5
print(calculadora("soma"))                      # Deve retornar 0
