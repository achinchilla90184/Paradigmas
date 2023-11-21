from config import *
from traffic_light import *
from object_counter import *
from threading import Thread

def loadData(config):
    #incia todos los semaforos en el sentido de las manecillas del reloj de A <-> D
    redLight = None
    for light in config.traffic_light.lights:
        if light.color == "red":
            redLight = light

    tlA = traffic_light(redLight.status, "A")
    tlB = traffic_light(redLight.status, "B")
    tlC = traffic_light(redLight.status, "C")
    tlD = traffic_light(redLight.status, "D")

    loadViaData(config)

    # Procesar informacion recibida de video concurrentemente para llenar la informacion de cada via
def loadViaData(config):
    threads = []
    for via in config.data_source.vias:
        print(via.path)
        thread = Thread(target=objectCounter, args=(via.path,))
        thread.start()
        threads.append(thread)
        break

    for i, thread in enumerate(threads):
        if thread.is_alive():
            thread.join()
