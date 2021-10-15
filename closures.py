def hacer_repetidor(n):
    def repetidor(cadena):
        return cadena*n
    return repetidor


def run():
    repetir_5 = hacer_repetidor(5)    
    print(repetir_5("Hola"))


if __name__ == '__main__':
    run()
