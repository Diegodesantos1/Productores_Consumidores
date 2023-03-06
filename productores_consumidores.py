from queue import Queue # Importamos la clase Queue
from threading import Thread # Importamos la clase Thread
import time # Importamos la librería time

q = Queue(10) # Creamos una cola de 10 elementos

def productor(nombre): # Definimos la función productor
    numero = 1 # Creamos una variable que nos servirá para contar las pizzas
    while True: # Creamos un bucle infinito
        q.join() # Esperamos a que la cola esté vacía
        q.put(numero) # Añadimos un elemento a la cola
        print(f"{nombre} está produciendo la pizza {numero}") # Mostramos un mensaje
        numero += 1 # Incrementamos el contador


def cliente(nombre): # Definimos la función cliente
    numero = 1 # Creamos una variable que nos servirá para contar las pizzas
    while True: # Creamos un bucle infinito
        print(f"{nombre} está comiendo la pizza {numero}") # Mostramos un mensaje
        numero += 1 # Incrementamos el contador
        q.task_done() # Indicamos que hemos terminado de consumir un elemento
        time.sleep(1) # Esperamos un segundo


