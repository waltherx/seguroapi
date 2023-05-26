class Alergia:

    def __init__(self, id=None, nombre="",descripcion="", gravedad="", reaccion="", paciente_id="") -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.gravedad= gravedad
        self.reaccion= reaccion
        self.paciente_id = paciente_id

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "gravedad": self.gravedad,
            "reaccion": self.reaccion,
            "paciente_id": self.paciente_id            
        }
