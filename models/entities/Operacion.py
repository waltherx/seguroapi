class Operacion:
    def __init__(
        self, id=None, tipo=None, fecha=None, descripcion=None, paciente_id=None
    ) -> None:
        self.id = id
        self.tipo = tipo
        self.fecha = fecha
        self.descripcion = descripcion
        self.paciente_id = paciente_id

    def to_JSON(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "paciente_id": self.paciente_id,
        }
