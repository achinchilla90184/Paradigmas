from src.config.config import *
from src.entities.traffic_light import *
from src.entities.via import *
from src.entities.intersection import *
from src.tools.object_detection_tracking import *
import time

def load_data_source(config):
    # incia todos los semaforos en el sentido de las manecillas del reloj de A <-> D, son dos semaforos por via porque funcionan en espejo
    vias = []

    # inicializa semaforos y vias
    for viaCfg in config.data_source.vias:
        tl = []
        tl1 = traffic_light(config.traffic_lights.red, viaCfg.name, viaCfg.pathA)
        tl2 = traffic_light(config.traffic_lights.red, viaCfg.name, viaCfg.pathB)
        tl.append(tl1)
        tl.append(tl2)
        v = via(viaCfg.name, 0, False, tl, config.traffic_lights.red)
        vias.append(v)
        # vehiculos de emergencia, cuantos autos, peatones
    return vias

# devuelve clases con la informacion analizada
def load_analyzed_data(vias):
    for v in vias:
        object_counter = 0

        for tl in v.traffic_lights:
            object_counter += count_objects_detected(tl.data_source)

        v.cars_counter = object_counter

    # Hay ambulancia?
    # Hay peatones?
    return vias
    
def process_data(data, colors):
    i = intersection(data)
    showTrafficLights(i.vias)
    # intersection.vias[0].emergency_vehicle= True
    isEmergency, emergencyVia = i.check_emergency_vehicles()
    if isEmergency:
        i.processEmergency(emergencyVia, colors)
        return
    priorityVia = i.get_priority_via()
    i.processPriority(priorityVia, colors)