def remove_duplicatas(lista: list) -> list:
    set_lista = set(lista)  # Converte em set que nao aceita duplicados
    return list(set_lista)


# lista: int = [1, 2, 2, 3, 4, 4, 5]
lista: int = [1, 2, 2, 3, 4, 4, 5, 9, 5, 5]

print(lista)
test = remove_duplicatas(lista)
print(test)

# Outra forma
print(list(dict.fromkeys(lista)))
