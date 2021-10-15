def read():
    numero = []
    with open("./archivos/numeros.txt","r", encoding="utf-8") as f:
        for line in f:
            numero.append(int(line))
    print(numero)


def write():
    nombres_cadena = ["Manuel","Julio", "gabriel","Nicolas"]
    # Si colocamos "a" sobre escribe, 
    # Si ponemos "w" vuelve a crear y escribir desde cero
    with open("./archivos/nombres.txt","a", encoding="utf-8") as f:
        for name in nombres_cadena:
            f.write(name)
            f.write("\n")

def run():
    write()


if __name__ == '__main__':
    run()