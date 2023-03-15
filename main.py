from threading import Thread
import time
from queue import Queue

buffer = Queue(30)
tam_buff = 30
buff = [0 for i in range(tam_buff + 1)]

def productor(id):
    milisegs = 0
    id_t = id
    while buffer.full() == False:
        buffer.put(id_t)
        milisegs += 1
        buff[buffer.qsize()] += 1
        time.sleep(0.001)
        print("El productor", id_t, "produjo")
        print("Buffer: ", buffer.qsize())
        print("Milisegundos: ", milisegs)
        print("-"*50)
    print("EL productor", id_t, "terminó")
    print("Buffer: ", buffer.qsize())
    print("Milisegundos: ", milisegs)
    print("")
    return


def consumidor(id):
    milisegs = 0
    id_t = id
    while buffer.empty() == False:
        buffer.get()
        milisegs += 1
        buff[buffer.qsize()] += 1
        time.sleep(0.001)
        print("Consumidor ", id_t, " consumió")
        print("Buffer: ", buffer.qsize())
        print("Milisegundos: ", milisegs)
        print("")
    print("Consumidor", id_t, "terminó")
    print("Buffer: ", buffer.qsize())
    print("Milisegundos: ", milisegs)
    print("-"*50)
    return


def main():
    total_productores = 4
    total_consumidores = 3
    productores = []
    consumidores = []
    start_time = time.time()
    for i in range(total_productores):
        productores.append(Thread(target=productor, args=(i,)))
        productores[i].start()
    for i in range(total_consumidores):
        consumidores.append(Thread(target=consumidor, args=(i,)))
        consumidores[i].start()
    for i in range(total_productores):
        productores[i].join()
    for i in range(total_consumidores):
        consumidores[i].join()
    print("Buffer: ", buffer.qsize())
    print("Total de productores: ", total_productores)
    print("Total de consumidores: ", total_consumidores)
    print("La ocupación del Buffer: ")
    for i in range(tam_buff + 1):
        print('Celda [', i, ']:', buff[i])
    print("Tiempo transcurrido: " + str(time.time() - start_time) + " segundos")
    return

if __name__ == '__main__':
    main()
