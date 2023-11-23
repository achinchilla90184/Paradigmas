from src.entities.traffic_light import *
class via:
    def  __init__(self, name, cars_counter, emergency_vehicle, traffic_lights, status) -> None:
        self.name = name
        self.cars_counter = cars_counter
        self.emergency_vehicle = emergency_vehicle
        self.traffic_lights = traffic_lights
        self.status = status
    
    def changeStatus(self, status):
        self.status = status
        for tl in self.traffic_lights:
            tl.change_color(status)