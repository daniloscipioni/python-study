def maior(inteiros: list[int]) -> int:
    return max(inteiros)


if __name__ == '__main__':
    lista: list[int] = [4, 7, 8, 2, 1, 9]
    print(f"Na lista: {lista} o maior valor é o {maior(lista)}")
