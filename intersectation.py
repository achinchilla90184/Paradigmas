class intersectation:
    def __init__(self, vias) -> None:
        self.vias = vias
    
    #cerrar todos los semaforos
    def panic(self):
        for via in self.vias:
            via.traffic_light.status = 0