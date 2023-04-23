class Vacuna:
    def __init__(
        self, id=None, nombre=None, dosis=None, paciente_id=None
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.dosis = dosis
        self.paciente_id = paciente_id

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "dosis": self.dosis,
            "paciente_id": self.paciente_id,
        }
