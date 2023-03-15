<h1 align = "center">Productores y consumidores</h1>

En este [repositorio](https://github.com/Diegodesantos1/Productores_Consumidores) queda resuelto el ejercicio de productores y consumidores.

<h2 align = "center">Planteamiento del problema</h2>

*La competencia por un recurso en memoria es un estado mediante en el cual uno o varios procesos tienen dependencia de algún recurso que podría no estar disponible en algún momento.*

*La dependencia de recursos en el estado con un solo proceso generalmente es secuencial, en donde el proceso dependiente tiene que consumir ciclos de reloj en espera de la liberación del recurso que necesita para continuar con su procesamiento.* 

*No obstante el tiempo de ejecución en el panorama secuencial se puede alargar mucho más cuando el recurso tarda en llegar o bien por labores de intentos de sincronización fuera de tiempo. Por tal motivo uno de los primeros planteamientos realizados para evitar la competencia de recursos es el uso de hilos de ejecución (threads) con la capacidad de comunicarse entre sí a través de un procedimiento de exclusión mutua. Sin embargo el mecanismo es pensado en un solo procesador.* 

*Más adelante nacieron los procesadores multicore, en donde cada core es capaz de ejecutar instrucciones independientes uno de otro, lo cuál ha modificado el esquema tradicional de programación secuencial. Aquí es donde nace el concepto de programación paralela.* 

*Un programa paralelo tiene la capacidad de ejecutar instrucciones en el mismo ciclo de reloj, pero para preservar sus beneficios de reducir enormemente los tiempos de ejecución, éstas instrucciones deben ser independientes de ejecución, es decir, reducir la sincronización hacia el mínimo de comunicación cuando existe dependencia de recursos, distribución de recursos en los procesadores y los mecanismos de exclusión mutua. Existen varios procedimientos de exclusión mutua.* 

*Un ejemplo clásico es el uso de semáforos en productores y consumidores y también han surgido otros problemas en base al acceso concurrente.*

*El acceso concurrente por parte de procesos productores y consumidores sobre un recurso común se realiza por medio un buffer de elementos. Los productores tratan de introducir elementos en el buffer de uno en uno, y los consumidores tratan de extraer elementos de uno en uno.*

*Para ejemplificar el desarrollo de un programa para productores y consumidores, asumimos que el productor es el que genera los recursos que van a utilizar los consumidores, por lo tanto los consumidores necesitan un proceso de sincronización con el productor para saber cuando el momento de consumir ha llegado.*

<h2 align = "center">Código</h2>

```python
from threading import Thread  # Importamos la librería Thread para poder usar hilos
import time  # Importamos la librería time para poder calcular el tiempo de ejecución
# Importamos la librería Queue para poder compartir información entre hilos
from queue import Queue

buffer = Queue(40)  # Creamos el buffer con una capacidad de 40
tam_buff = 40  # Creamos una variable para almacenar el tamaño del buffer
# Creamos una lista para almacenar la ocupación del buffer
buff = [0 for i in range(tam_buff + 1)]


def productor(id):  # Creamos la función productor
    milisegs = 0  # Creamos una variable para almacenar los milisegundos
    id_t = id  # Creamos una variable para almacenar el id del productor
    while buffer.full() == False:  # Mientras el buffer no esté lleno
        buffer.put(id_t)  # Agregamos un elemento al buffer
        milisegs += 1  # Incrementamos los milisegundos
        buff[buffer.qsize()] += 1  # Incrementamos la ocupación del buffer
        time.sleep(0.001)  # Hacemos una pausa de 1 milisegundo
        # Imprimimos el id del productor
        print("El productor", id_t, "produjo")
        print("Buffer: ", buffer.qsize())  # Imprimimos el tamaño del buffer
        print("Milisegundos: ", milisegs)  # Imprimimos los milisegundos
        print("-"*50)  # Imprimimos una línea para separar
    print("El productor", id_t, "terminó")  # Imprimimos el id del productor
    print("Buffer: ", buffer.qsize())  # Imprimimos el tamaño del buffer
    print("Milisegundos: ", milisegs)  # Imprimimos los milisegundos
    print("-"*50)  # Imprimimos una línea para separar
    return


def consumidor(id):  # Creamos la función consumidor
    milisegs = 0  # Creamos una variable para almacenar los milisegundos
    id_t = id  # Creamos una variable para almacenar el id del consumidor
    while buffer.empty() == False:  # Mientras el buffer no esté vacío
        buffer.get()  # Eliminamos un elemento del buffer
        milisegs += 1  # Incrementamos los milisegundos
        buff[buffer.qsize()] += 1  # Incrementamos la ocupación del buffer
        time.sleep(0.001)  # Hacemos una pausa de 1 milisegundo
        # Imprimimos el id del consumidor
        print("Consumidor ", id_t, " consumió")
        print("Buffer: ", buffer.qsize())  # Imprimimos el tamaño del buffer
        print("Milisegundos: ", milisegs)  # Imprimimos los milisegundos
        print("-"*50)  # Imprimimos una línea para separar
    print("Consumidor", id_t, "terminó")  # Imprimimos el id del consumidor
    print("Buffer: ", buffer.qsize())  # Imprimimos el tamaño del buffer
    print("Milisegundos: ", milisegs)  # Imprimimos los milisegundos
    print("-"*50)  # Imprimimos una línea para separar
    return


def main():

    # Creamos la función main
    total_productores = 4  # Creamos una variable para almacenar el total de productores
    total_consumidores = 3  # Creamos una variable para almacenar el total de consumidores
    productores = []  # Creamos una lista para almacenar los productores
    consumidores = []  # Creamos una lista para almacenar los consumidores
    start_time = time.time()  # Creamos una variable para almacenar el tiempo de inicio
    for i in range(total_productores):  # Creamos los productores
        # Agregamos los productores a la lista
        productores.append(Thread(target=productor, args=(i,)))
        productores[i].start()  # Iniciamos los productores
    for i in range(total_consumidores):  # Creamos los consumidores
        # Agregamos los consumidores a la lista
        consumidores.append(Thread(target=consumidor, args=(i,)))
        consumidores[i].start()  # Iniciamos los consumidores
    for i in range(total_productores):  # Esperamos a que terminen los productores
        productores[i].join()  # Esperamos a que terminen los productores
    for i in range(total_consumidores):  # Esperamos a que terminen los consumidores
        consumidores[i].join()  # Esperamos a que terminen los consumidores
    print("Buffer: ", buffer.qsize())  # Imprimimos el tamaño del buffer
    # Imprimimos el total de productores
    print("Total de productores: ", total_productores)
    # Imprimimos el total de consumidores
    print("Total de consumidores: ", total_consumidores)
    print("La ocupación del Buffer: ")  # Imprimimos la ocupación del buffer
    for i in range(tam_buff + 1):  # Recorremos el buffer
        # Imprimimos la ocupación del buffer
        print('Celda [', i, ']:', buff[i])
    print("Tiempo transcurrido: " + str(time.time() - start_time) +
          " segundos")  # Imprimimos el tiempo de ejecución
    return


if __name__ == '__main__':
    main()
    
```

<h2 align = "center">Ejemplo aplicado</h2>

En este ejemplo voy a usar 4 productores y 3 consumidores

![image](https://user-images.githubusercontent.com/91721855/225366747-640530ad-14a0-4f88-90c8-54c6e11cee5a.png)

Y un tamaño de buffer de 40

![image](https://user-images.githubusercontent.com/91721855/225366884-76399bc4-0199-4e1a-8599-e1639a9828a4.png)

Con esto comprobaremos el uso del módulo Queue para poder compartir información entre hilos, generando la siguiente ejecución:

![gif](https://github.com/Diegodesantos1/Productores_Consumidores/blob/main/ejecucion.gif)

Con los siguientes resultados de la ocupación del buffer:

![image](https://user-images.githubusercontent.com/91721855/225369458-a9f08a82-0bef-4d11-9362-bc85999e8f57.png)

<h2 align = "center">Conclusiones</h2>

*Gracias al módulo Queue se ha podido compartir información entre hilos, para que puedan "producir" y "consumir" recursos y además se puede ver la ocupación del buffer y los milisegundos que ha tardado en cada proceso. Para finalizar el programa he calculado el tiempo de ejecución con el módulo time.*
