from config import *
from traffic_light import *
from via import *
from intersectation import *

#devuelve clases con la informacion cargada
def loadData(config):
    #incia todos los semaforos en el sentido de las manecillas del reloj de A <-> D, son dos semaforos por via porque funcionan en espejo
    vias = []
    tl = []

    # Inicializa semaforos y vias
    for viaCfg in config.data_source.vias:
        tl1 = traffic_light(config.traffic_lights.red, viaCfg.name)
        tl2 = traffic_light(config.traffic_lights.red, viaCfg.name)
        tl.append(tl1)
        tl.append(tl2)
        v = via(viaCfg.name, 0, False, tl, viaCfg.path)
        vias.append(v)
        # vehiculos de emergencia, cuantos autos, peatones
    # Debe llamar a funcion de input de los videos
    # Hay ambulancia?
    # Cuantos objetos?
    # Hay peatones?
    return vias
    
def processData(config, viasData):
    i = intersectation(viasData)
    # print(i.vias[0].traffic_lights[0].status)
    if i.checkEmergencyVehicles(config.traffic_lights):
        return
    # print(i.vias[0].traffic_lights[0].status)