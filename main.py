from threading import Thread # Importamos la librería Thread para poder usar hilos
import time # Importamos la librería time para poder calcular el tiempo de ejecución
from queue import Queue # Importamos la librería Queue para poder compartir información entre hilos

buffer = Queue(40) # Creamos el buffer con una capacidad de 40
tam_buff = 40 # Creamos una variable para almacenar el tamaño del buffer
buff = [0 for i in range(tam_buff + 1)] # Creamos una lista para almacenar la ocupación del buffer

def productor(id): # Creamos la función productor
    milisegs = 0 # Creamos una variable para almacenar los milisegundos
    id_t = id # Creamos una variable para almacenar el id del productor
    while buffer.full() == False: # Mientras el buffer no esté lleno
        buffer.put(id_t) # Agregamos un elemento al buffer
        milisegs += 1 # Incrementamos los milisegundos
        buff[buffer.qsize()] += 1 # Incrementamos la ocupación del buffer
        time.sleep(0.001) # Hacemos una pausa de 1 milisegundo
        print("El productor", id_t, "produjo") # Imprimimos el id del productor
        print("Buffer: ", buffer.qsize()) # Imprimimos el tamaño del buffer
        print("Milisegundos: ", milisegs) # Imprimimos los milisegundos
        print("-"*50) # Imprimimos una línea para separar
    print("El productor", id_t, "terminó") # Imprimimos el id del productor
    print("Buffer: ", buffer.qsize()) # Imprimimos el tamaño del buffer
    print("Milisegundos: ", milisegs) # Imprimimos los milisegundos
    print("-"*50)  # Imprimimos una línea para separar
    return 


def consumidor(id): # Creamos la función consumidor
    milisegs = 0 # Creamos una variable para almacenar los milisegundos
    id_t = id # Creamos una variable para almacenar el id del consumidor
    while buffer.empty() == False: # Mientras el buffer no esté vacío
        buffer.get() # Eliminamos un elemento del buffer
        milisegs += 1 # Incrementamos los milisegundos
        buff[buffer.qsize()] += 1 # Incrementamos la ocupación del buffer
        time.sleep(0.001) # Hacemos una pausa de 1 milisegundo
        print("Consumidor ", id_t, " consumió") # Imprimimos el id del consumidor
        print("Buffer: ", buffer.qsize()) # Imprimimos el tamaño del buffer
        print("Milisegundos: ", milisegs) # Imprimimos los milisegundos
        print("-"*50) # Imprimimos una línea para separar
    print("Consumidor", id_t, "terminó") # Imprimimos el id del consumidor
    print("Buffer: ", buffer.qsize()) # Imprimimos el tamaño del buffer
    print("Milisegundos: ", milisegs) # Imprimimos los milisegundos
    print("-"*50) # Imprimimos una línea para separar
    return


def main(): # Creamos la función main
    total_productores = 4 # Creamos una variable para almacenar el total de productores
    total_consumidores = 3 # Creamos una variable para almacenar el total de consumidores
    productores = [] # Creamos una lista para almacenar los productores
    consumidores = [] # Creamos una lista para almacenar los consumidores
    start_time = time.time() # Creamos una variable para almacenar el tiempo de inicio
    for i in range(total_productores): # Creamos los productores
        productores.append(Thread(target=productor, args=(i,))) # Agregamos los productores a la lista
        productores[i].start() # Iniciamos los productores
    for i in range(total_consumidores): # Creamos los consumidores
        consumidores.append(Thread(target=consumidor, args=(i,))) # Agregamos los consumidores a la lista
        consumidores[i].start() # Iniciamos los consumidores
    for i in range(total_productores): # Esperamos a que terminen los productores
        productores[i].join() # Esperamos a que terminen los productores
    for i in range(total_consumidores): # Esperamos a que terminen los consumidores
        consumidores[i].join() # Esperamos a que terminen los consumidores
    print("Buffer: ", buffer.qsize()) # Imprimimos el tamaño del buffer
    print("Total de productores: ", total_productores) # Imprimimos el total de productores
    print("Total de consumidores: ", total_consumidores) # Imprimimos el total de consumidores
    print("La ocupación del Buffer: ") # Imprimimos la ocupación del buffer
    for i in range(tam_buff + 1): # Recorremos el buffer
        print('Celda [', i, ']:', buff[i]) # Imprimimos la ocupación del buffer
    print("Tiempo transcurrido: " + str(time.time() - start_time) + " segundos") # Imprimimos el tiempo de ejecución
    return

if __name__ == '__main__':
    main()
