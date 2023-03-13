class Hospital:
    def __init__(
        self, id=None, nombre=None, direccion=None, lat=None, long=None
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.lat = lat
        self.long = long

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "lat": self.lat,
            "long": self.long,
        }
