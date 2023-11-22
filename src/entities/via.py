from src.entities.traffic_light import *
class via:
    def  __init__(self, name, cars_counter, emergency_vehicle, traffic_lights) -> None:
        self.name = name
        self.cars_counter = cars_counter
        self.emergency_vehicle = emergency_vehicle
        self.traffic_lights = traffic_lights

    def calculate_via_value(self, config):
        self.name = ""

    def set_via_status(self, status):
        for tl in self.traffic_lights:
            tl.change_color(status)