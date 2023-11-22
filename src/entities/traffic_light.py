class traffic_light:
    def __init__(self, status, name, data_source) -> None:
        self.status = status
        self.name = name
        self.data_source = data_source
    def change_color(self, status):
        self.status = status