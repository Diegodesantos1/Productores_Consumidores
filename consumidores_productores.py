import threading
import time
import random

sem = threading.Semaphore(0)
mutex = threading.Semaphore(1)
buffer = []

