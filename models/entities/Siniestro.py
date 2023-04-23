class Siniestro:
    def __init__(
        self, id=None, descripccion=None, fecha=None, lat=None, long=None, paciente_id=None
    ) -> None:
        self.id = id
        self.descripccion = descripccion
        self.fecha = fecha
        self.lat = lat
        self.long = long
        self.paciente_id = paciente_id

    def to_JSON(self):
        return {
            "id": self.id,
            "descripccion": self.descripccion,
            "fecha": self.fecha,
            "lat": self.lat,
            "long": self.long,
            "paciente_id": self.paciente_id,
        }
