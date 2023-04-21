class Ambulancia:
    def __init__(
        self,
        id=None,
        modelo=None,
        marca=None,
        anio=None,
        placa=None,
        capacidad=None,
        lat=None,
        long=None,
        estado=None,
    ) -> None:
        self.id = id
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.placa = placa
        self.capacidad = capacidad
        self.lat = lat
        self.long = long
        self.estado = estado

    def to_JSON(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "marca": self.marca,
            "anio": self.anio,
            "placa": self.placa,
            "capacidad": self.capacidad,
            "lat": self.lat,
            "long": self.long,
            "estado": self.estado,
        }
