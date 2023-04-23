class Chofer:
    def __init__(
        self,
        id=None,
        licencia=None,
        categoria=None,
        estado=None,
        id_ambulancia=None,
        ci_persona=None,
    ) -> None:
        self.id = id
        self.licencia = licencia
        self.categoria_licencia = categoria
        self.estado = estado
        self.id_ambulancia = id_ambulancia
        self.ci_persona = ci_persona

    def to_JSON(self):
        return {
            "id": self.id,
            "licencia": self.licencia,
            "categoria": self.categoria_licencia,
            "estado": self.estado,
            "id_ambulancia": self.id_ambulancia,
            "ci_persona": self.ci_persona,
        }
