"""
Entendo o *args

- o *args e um parametro como outro qualquer. Isso significa que voce podera 
chamar de qualquer coisa, desde que comece com asterisco

Por exemplo
*xis

Mas por convencao, utilizamos *args para defini-lo

Mas o que e args?

O Parametro *args utilizado em uma funcao, coloca os valores extras informados como
entrada em uma tupla e tuplas sao imutaveis



def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(1, 2, 3))
# print(soma_todos_numeros(1, 2, 3)) TypeError
# print(soma_todos_numeros(1, 2, 3, 6)) TypeError


# Entendendo o *args


def soma_todos_numeros(nome, sobrenome, *args):
    return f'{nome} - {sobrenome} - {sum(args)}'


print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 1, 2))
print(soma_todos_numeros('Angelina', 'Jolie', 1, 2, 3, 4))

# Outro exemplo do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek!'
    return 'Eu nao sei quem e voce'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

# O asterisco serve para que informemos ao Python que estamos passando como argumento uma colecao de dados
# Desta forma ele sabera que precisara desempacotar esses dados.
print(soma_todos_numeros(*numeros))
