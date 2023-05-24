class Documento:
    def __init__(
        self,
        id=None,
        nombre=None,
        url=None,
        tipo=None,
        descripcion=None,
        fechaSubida=None,
        paciente_id=None,
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.url = url
        self.tipo = tipo
        self.descripcion = descripcion
        self.fechaSubida = fechaSubida
        self.paciente_id = paciente_id

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre":self.nombre,
            "url": self.url,
            "tipo": self.tipo,
            #"descripcion": self.descripcion,
            "fechaSubida": self.fechaSubida,
            "paciente_id": self.paciente_id,
        }
