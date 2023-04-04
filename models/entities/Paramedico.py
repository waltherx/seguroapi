class Paramedico:
    def __init__(
        self,
        id=None,
        especialidad=None,
        id_ambulancia=None,
    ) -> None:
        self.id = id
        self.especialidad = especialidad
        self.id_ambulancia = id_ambulancia

    def to_JSON(self):
        return {
            "id": self.id,
            #"licencia_medica": self.licencia_medica,
            "especialidad": self.especialidad,
            "id_ambulancia": self.id_ambulancia,
        }
