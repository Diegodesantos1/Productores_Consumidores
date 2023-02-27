import threading
import time
import random

sem = threading.Semaphore(0)
mutex = threading.Semaphore(1)
buffer = []

def productor():
    global buffer
    while True:
        time.sleep(random.random())
        dato = random.randint(1, 100)
        mutex.acquire()
        buffer.append(dato)
        print ("productor:", dato)
        mutex.release()
        sem.release()

def consumidor():
    global buffer
    while True:
        sem.acquire()
        mutex.acquire()
        dato = buffer.pop()
        print ("consumidor:", dato)
        mutex.release()

