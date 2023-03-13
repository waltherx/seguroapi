class Documento:
    def __init__(
        self,
        id=None,
        url=None,
        tipo=None,
        descripcion=None,
        fechaSubida=None,
        idper=None,
    ) -> None:
        self.id = id
        self.url = url
        self.tipo = tipo
        self.descripcion = descripcion
        self.fechaSubida = fechaSubida
        self.idper = idper

    def to_JSON(self):
        return {
            "id": self.id,
            "url": self.url,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "fechaSubida": self.fechaSubida,
            "idper": self.idper,
        }
