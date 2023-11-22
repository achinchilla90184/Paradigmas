from src.entities.traffic_light import *
class via:
    def  __init__(self, name, cars_counter, emergency_vehicle, traffic_lights, data_source) -> None:
        self.name = name
        self.cars_counter = cars_counter
        self.emergency_vehicle = emergency_vehicle
        self.traffic_lights = traffic_lights
        self.data_source = data_source

    def calculateViaValue(self, config):
        self.name = ""

    def setViaStatus(self, status):
        for tl in self.traffic_lights:
            tl.changeColor(status)