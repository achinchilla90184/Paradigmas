class intersectation:
    def __init__(self, vias) -> None:
        self.vias = vias
    
    #cerrar todos los semaforos
    def checkEmergencyVehicles(self, colors):
        for via in self.vias:
            if via.emergency_vehicle:
                via.setViaStatus(colors.green)
                return via.emergency_vehicle