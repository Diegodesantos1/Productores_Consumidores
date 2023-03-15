from threading import Thread
import time
from queue import Queue

buffer = Queue(30)
tam_buff = 30
buff = [0 for i in range(tam_buff + 1)]

