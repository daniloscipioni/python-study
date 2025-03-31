import logging

# Configuração básica para os logs
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def logar_exec(**kwargs):

    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.debug(f"Executando função: {func.__name__}")
            logging.debug(f"Argumentos: args={args}, kwargs={kwargs}")
            print(kwargs)
            resultado = func(*args, **kwargs)
            logging.debug(f"Função {func.__name__} retornou: {resultado}")

            return resultado
        return wrapper
    return decorator


@logar_exec(ex="teste")
def diga_oi(**kwargs):
    print(kwargs)


diga_oi(test="Olá")
