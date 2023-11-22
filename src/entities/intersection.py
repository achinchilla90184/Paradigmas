class intersectation:
    def __init__(self, vias) -> None:
        self.vias = vias
    
    #cerrar todos los semaforos
    def check_emergency_vehicles(self, colors):
        for via in self.vias:
            if via.emergency_vehicle:
                via.set_via_status(colors.green)
                return via.emergency_vehicle