from classes import Coche, Surtidor, Gasolinera
import time
import random
from queue import Queue

cola = Queue()
t = 15
n = 4
        

def generar_coche():
    for i in range(50):
        coche = Coche("Coche %s" % i, random.randint(0,3), Gasolinera("Gasolinera","Coche %s" % i, cola))
        coche.start()
        time.sleep(t)

if __name__ == "__main__":
    generar_coche()