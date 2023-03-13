class Siniestro:
    def __init__(
        self, id=None, descripccion=None, fecha=None, lat=None, long=None, idper=None
    ) -> None:
        self.id = id
        self.descripccion = descripccion
        self.fecha = fecha
        self.lat = lat
        self.long = long
        self.idper = idper

    def to_JSON(self):
        return {
            "id": self.id,
            "descripccion": self.descripccion,
            "fecha": self.fecha,
            "lat": self.lat,
            "long": self.long,
            "idper": self.idper,
        }
