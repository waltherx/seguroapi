class Paramedico:
    def __init__(
        self,
        id=None,
        especialidad=None,
        id_ambulancia=None,
        ci_persona=None,
    ) -> None:
        self.id = id
        self.especialidad = especialidad
        self.id_ambulancia = id_ambulancia
        self.ci_persona = ci_persona

    def to_JSON(self):
        return {
            "id": self.id,
            "especialidad": self.especialidad,
            "id_ambulancia": self.id_ambulancia,
            "ci_persona": self.ci_persona
        }
