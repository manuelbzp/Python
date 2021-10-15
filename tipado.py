# Ejemplo de tipado static
def es_palindromo(cadena: str) -> bool:
    cadena = cadena.replace(" ","").lower()
    return cadena == cadena[::-1]


def run():
    print(es_palindromo(1000))


if __name__ == '__main__':
    run()