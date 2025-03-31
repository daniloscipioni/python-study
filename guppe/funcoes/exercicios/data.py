
def get_data_extenso(date: str) -> None:
    date_split = date.split("/")
    month = ""
    if date_split[1] == "01":
        month = "Janeiro"
    elif date_split[1] == "02":
        month = "Fevereiro"
    elif date_split[1] == "03":
        month = "Março"
    elif date_split[1] == "04":
        month = "Abril"
    elif date_split[1] == "05":
        month = "Maio"
    elif date_split[1] == "06":
        month = "Junho"
    elif date_split[1] == "07":
        month = "Julho"
    elif date_split[1] == "08":
        month = "Agosto"
    elif date_split[1] == "09":
        month = "Setembro"
    elif date_split[1] == "10":
        month = "Outubro"
    elif date_split[1] == "11":
        month = "Novembro"
    elif date_split[1] == "12":
        month = "Dezembro"
    else:
        month = "Desconhecido"

    print(f"{int(date_split[0])} de {month} de {int(date_split[2])}")


if __name__ == '__main__':
    get_data_extenso("01/01/2024")
