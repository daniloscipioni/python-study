"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

[1] - Utilize Camel Case para nomes de classes;
class Calculadora:
    pass

class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funcoes ou variaveis

def soma():
    pass

def soma_dois():
    pass

numero = 4

[3] - Utilize 4 espacos para identacao (nao use tab)
if 'a' in 'banana':
    print('tem')

[4] Linhas em branco
- Separar funcoes e definicoes de classe com duas linhas em branco
- Metdoos dentro de uma classe devem ser separados por uma unica linha em branco

[5] Imports
- Imports devem ser sempre feitos em linhas separadas

# Nao ha problemas em utilizar
from types import StringType, ListType

caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType,
    ListType
)

- Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings e antes de constantes ouy variavies globais

[6] -  Espacos em expressoes e instrucoes

#Nao faca:
funcao( algo[ 1 ], {outro: 2 } )

#Faca
funcao(algo[1], {outro:2})

[7] - Termine sempre uma instrucao com uma nova linha
"""




