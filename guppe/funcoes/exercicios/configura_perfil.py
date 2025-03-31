def configurar_perfil(nome, idade, **kwags):
    """
    Configura o perfil do usuario com nome, idade e caracteristicas adicionais.
    """
    perfil = {"nome": nome, "idade": idade}
    perfil.update(kwags)

    return perfil


perfil1 = configurar_perfil("Alice", 25, cidade="São Paulo", profissão="Engenheira")
perfil2 = configurar_perfil("Carlos", 30, hobby="Fotografia", idioma="Espanhol")
perfil3 = configurar_perfil("João", 18)

# Deve retornar {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo', 'profissão': 'Engenheira'}
print(perfil1)
# Deve retornar {'nome': 'Carlos', 'idade': 30, 'hobby': 'Fotografia', 'idioma': 'Espanhol'}
print(perfil2)
print(perfil3)  # Deve retornar {'nome': 'João', 'idade': 18}
