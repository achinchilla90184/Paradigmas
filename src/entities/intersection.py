from src.entities.via import *
import time
class intersection:
    def __init__(self, vias) -> None:
        self.vias = vias
    
    #revisar que no hayan vehiculos de emergencia
    def check_emergency_vehicles(self):
        for via in self.vias:
            if via.emergency_vehicle:
                return via.emergency_vehicle, via
        return False, None
            
    def get_priority_via(self):
        priorityVia = via("", 0, False, [], 0)
        for v in self.vias:
            if priorityVia.cars_counter < v.cars_counter:
                priorityVia = v
        return priorityVia
        
    def processPriority(self, priorityVia, colors):
            # vias que no son de emergencia en amarillo por 5 segundos
            for via in self.vias:
                if  via.status == colors.yellow:
                    via.changeStatus(colors.yellow)
            showTrafficLights(self.vias)
            time.sleep(5)
            for via in self.vias:
            # vias que no son de emergencia en rojo
                via.changeStatus(colors.red)
            showTrafficLights(self.vias)
            # vias de emergencia en verde
            priorityVia.changeStatus(colors.green)
            showTrafficLights(self.vias)

    def processEmergency(self, emergencyVia, colors):
        # vias que no son de emergencia en amarillo por 5 segundos
        for via in self.vias:
            if via.name != emergencyVia.name and via.status == colors.yellow:
                via.changeStatus(colors.yellow)
        showTrafficLights(self.vias)
        time.sleep(5)
        for via in self.vias:
        # vias que no son de emergencia en rojo
            if via.name != emergencyVia.name:
                via.changeStatus(colors.red)
        showTrafficLights(self.vias)
        # vias de emergencia en verde
        emergencyVia.changeStatus(colors.green)
        showTrafficLights(self.vias)

# just for testing
def showTrafficLights(viasData):
    print("\n")
    for v in viasData:
        for tl in v.traffic_lights:
            print("via " + v.name + ". tl " + tl.name + " . status " + str(tl.status) + ". cars counter " + str(v.cars_counter))
            # object_counter += count_objects_detected(tl.data_source)
            if tl.status == 2:
                verde()
            if tl.status == 0:
                rojo()