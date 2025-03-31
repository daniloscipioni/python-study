"""
**kwargs

Por exemplo
*xis

Mas por convencao, utilizamos *kwargs para defini-lo

Este e mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parametros nomeados e transforma esses parametros
extras em um dicionario


# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} e {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parametros *args e **kwargs nao sao obrigatorios
cores_favoritas()
cores_favoritas(marcos='verde')



def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu cumprimento'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Nao te conheco'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funcoes, podemos ter (NESTA ORDEM):

- Parametros obrigatorios;
- *args;
- Parametros default (Nao obrigatorios);
- **kwargs




def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(35, 'Danilo')
print('-----')
minha_funcao(16, 'Felicity', 4, 5, 3, solteiro=True)
print('-----')
minha_funcao(34, 'Felipe', eu='Nao', voce='Vai')
print('-----')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)



# Por que e importante a ordem dos parametros

# Funcao com a ordem correta de parametros
def mostra_info(a, b, *args, intrutor='Geek', **kwargs):
    return [a, b, args, intrutor, kwargs]


# Funcao com a ordem incorreta de parametros
def mostra_info_2(a, b,  intrutor='Geek', *args, **kwargs):
    return [a, b, args, intrutor, kwargs]


# [1, 2, (3,), 'Geek', {'sobrenome': 'Univerisity', 'cargo': 'Intrutor'}]
print(mostra_info(1, 2, 3, sobrenome='Univerisity', cargo='Intrutor'))

# [1, 2, (), 3, {'sobrenome': 'Univerisity', 'cargo': 'Intrutor'}]
print(mostra_info_2(1, 2, 3, sobrenome='Univerisity', cargo='Intrutor'))


# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(nome='Felicity', sobrenome='Jones'))
print(mostra_nomes(**nomes))
"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a+b+c)


numeros_lista = [3, 6, 7]
numeros_tupla = (3, 6, 7)
numeros_conjunto = {3, 6, 7}

soma_multiplos_numeros(*numeros_lista)
soma_multiplos_numeros(*numeros_tupla)
soma_multiplos_numeros(*numeros_conjunto)

# OBS: Os nomes da chave em um dicionario devem ser o mesmo dos parametros da funcao
dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# Error TypeError
dicionario_1 = dict(d=1, e=2, f=3)
# soma_multiplos_numeros(**dicionario_1)

dicionario = dict(a=1, b=2, c=3, nome='Geek')
soma_multiplos_numeros(**dicionario, lang='Python')
