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
