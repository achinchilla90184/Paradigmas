class traffic_light:
    def __init__(self, status, name) -> None:
        self.status = status
        self.name = name
    def changeColor(self, status):
        self.status = status