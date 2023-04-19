class Chofer:
    def __init__(
        self,
        id=None,
        licencia=None,
        categoria_licencia=None,
        estado=None,
        id_ambulancia=None,
        user_id=None,
    ) -> None:
        self.id = id
        self.licencia = licencia
        self.categoria_licencia = categoria_licencia
        self.estado = estado
        self.id_ambulancia = id_ambulancia
        self.user_id = user_id

    def to_JSON(self):
        return {
            "id": self.id,
            "licencia": self.licencia,
            "categoria_licencia": self.categoria_licencia,
            "estado": self.estado,
            "id_ambulancia": self.id_ambulancia,
            "user_id": self.user_id,
        }
