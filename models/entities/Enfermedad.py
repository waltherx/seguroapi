class Enfermedad:
    def __init__(
        self,
        id=None,
        nombre=None,
        descripcion=None,
        causa=None,
        sintoma=None,
        diagnostico=None,
        paciente_id=None,
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.causa = causa
        self.sintoma = sintoma
        self.diagnostico = diagnostico
        self.paciente_id = paciente_id

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "causa": self.causa,
            "sintoma": self.sintoma,
            "diagnostico": self.diagnostico,
            "paciente_id": self.paciente_id,
        }   
