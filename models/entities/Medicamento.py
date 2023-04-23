class Medicamento:
    def __init__(
        self,
        id=None,
        nombre=None,
        descripcion=None,
        cantidad=None,
        unidad=None,
        paciente_id=None,
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.unidad = unidad
        self.paciente_id = paciente_id

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "cantidad": self.cantidad,
            "unidad": self.unidad,
            "paciente_id": self.paciente_id,
        }
