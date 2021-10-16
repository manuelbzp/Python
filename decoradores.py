#ESte es un ejemplo de decoradores
from datetime import datetime

# wrapper en ingles es envoltura
def execution_time(func):
    def wrapper(*arg,**kwargs):
        initial_time = datetime.now() 
        func(*arg,**kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print("Pasaron: "+str(time_elapse.total_seconds())+" segundos")
    return wrapper

@execution_time
def random_fun():
    for _ in range(1,1000000):
        pass

@execution_time
def suma(a: int, b:int ) -> int:
    return a+b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola: "+nombre)

random_fun()
suma(2,2)
saludo()