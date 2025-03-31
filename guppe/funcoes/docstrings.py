"""
Documentando funcoes com Docstrings

Podemos ter acesso a documentacao de uma funcao em Python utilizando a propridade especial __doc__

Podemos ainda fazer acesso a documantacao com a funcao help()


print(help(print))

# Exemplos


def diz_oi():

    \""" Uma funcao simples que retrona a string 'Oi!'\"""
    #return "Oi! "


print(diz_oi())

print(diz_oi.__doc__)  # Imprime a docstring

print(help(diz_oi))
"""


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' informada
    : param numero: Numero que desejamos gerar o exponencial.
    : param pontencia: Potencia que queremos gerar o exponencial. Por padrao e 2.
    : return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia


# A mesma coisa
print(exponencial.__doc__)
print(help(exponencial))
