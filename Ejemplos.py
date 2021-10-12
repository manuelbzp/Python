def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    lista_poblacion = {
        'Argentina':20,
        'Brasil':50,
        'Colombia':10
    }

    print(lista_poblacion)
    for pais in lista_poblacion.keys():
        print([pais])

    for valor in lista_poblacion.values():
        print(valor)

    numero = 10
    if numero > 5:
        print("Es mayor a 5")

# aver que sale en el git
#Este es otro cambio 
if __name__ == '__main__':
    run()