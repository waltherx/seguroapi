class Paramedico:
    def __init__(
        self,
        id=None,
        especialidad=None,
        id_ambulancia=None,
        user_id=None,
    ) -> None:
        self.id = id
        self.especialidad = especialidad
        self.id_ambulancia = id_ambulancia
        self.user_id = user_id

    def to_JSON(self):
        return {
            "id": self.id,
            #"licencia_medica": self.licencia_medica,
            "especialidad": self.especialidad,
            "id_ambulancia": self.id_ambulancia,
            "user_id": self.user_id,
        }
