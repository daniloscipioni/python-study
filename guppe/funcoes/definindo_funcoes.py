"""
Definindo funcoes

"""

cores = ['verde', 'amarelo', 'azul', 'branco']

# Funcoes integradas (Built in) do python print()

print(cores)

curso = 'Programacao em python'

print(curso)


cores.append('roxo')

"""
Parametro obrigatorio
def quadrado(numero):
    return numero ** 2
"""

# Funcoes de parametros opcionais
# Os parametros com valores default devem sempre estar ao final da declaracao
"""
Errado
def exponencial(numero=2, potencia):
    return numero ** potencia
"""


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2))  # Por padrao eleva ao quadrado
print(exponencial(2, 3))  # Por padrao eleva a potencia informada


# Variaveis globais
instrutor = 'geek'


def diz_oi():
    #   A variavel local vai ter prioridade
    instrutor = 'Python'
    return f'Oi {instrutor}'


print(diz_oi())

# Se puder evitar variaveis globais é melhor
"""
total = 0


def incrementa():
    total = total + 1 # UnboundLocalError
    return total

# A variavel local nao foi inicializada
print(incrementa())


total = 0


def incrementa():
    global total  # avisando que queremos utilizar a variavel global

    total = total + 1  # UnboundLocalError
    return total


# A variavel local nao foi inicializada
print(incrementa()) # 1
print(incrementa()) # 2
print(incrementa()) # 3

"""
# Podemos ter funcoes que sao declaradas dentro de funcoes, e tambem tem uma forma especial de escopo de variaveis


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # não é local e nem global, é a de dentro da funcao anterior
        contador = contador + 1
        return contador
    return dentro()


print(fora())  # 1
print(fora())  # 1
print(fora())  # 1
