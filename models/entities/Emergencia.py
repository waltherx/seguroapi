class Emergencia:
    def __init__(
        self,
        id=None,
        fecha=None,
        descripcion=None,
        estado=None,
        ambulancia_id=None,
        hospital_id=None,
    ) -> None:
        self.id = id
        self.fecha = fecha
        self.descripcion = descripcion
        self.estado = estado
        self.ambulancia_id = ambulancia_id
        self.hospital_id = hospital_id

    def to_JSON(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "ambulancia_id": self.ambulancia_id,
            "hospital_id": self.hospital_id,
        }
        
    def __str__(self):
        return f"{self.fecha}, {self.descripcion}"
    
