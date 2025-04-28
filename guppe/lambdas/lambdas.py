
"""
Utilizando lambdas

Conhecidas por expressoes Lambdas, ou simplesmente Lambdas, sao funcoes sem nome, ou seja, 
funcoes anonimas

Funcao em Python

def soma(a, b):
    return a + b



def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressao Lambda

lambda x: 3 * x + 1

# Como utilizar a expressao lambda


def calc(x): return 3 * x + 1


print(calc(4))
print(calc(7))


# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY  ', 'jones   '))


# Em funcoes Python podemos ter nenhuma ou varias entradas. Em Lambdas tambem

amar = lambda : 'Como nao amar Python? '
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x*y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ....., xn: <expressao>

print(amar)
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Obs: Se passarmos mais argumentos do que parametros esperados, teremos TypeError


# Outros exemplos

autores = ['Isaac Asimov','Ray Basd','Robert Hasd','Artur C. Clark','Frank Herbert','Orson Scot Card',
           'Douglas Addams','H. G. Wells','Leit Brasad']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""

# Funcao Quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a funcao
def geradora_funcao_quadratica(a, b, c):
    """Retorna a funcao f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(2, 3, -5)(2))