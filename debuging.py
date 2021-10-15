def divisores(num):
    divisores = []
    for i in range(1,num+1):
        if num % i == 0:
            divisores.append(i)
    return divisores        

def run():
    num = input("Ingresa un numero")
    assert num.isnumeric(), "Deber ingresar un numero"
    assert num>0, "Debes ingresar un numero positivo"
    print(divisores(int(num)))
    print("Termino")

if __name__ =='__main__':
    run()