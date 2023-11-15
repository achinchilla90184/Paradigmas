from config import *
from traffic_light import *

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

    # Procesar informacion recibida de video concurrentemente para llenar la informacion de cada via