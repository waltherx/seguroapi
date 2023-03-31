class Vacuna:
    def __init__(
        self, id=None, nombre=None, dosis=None, ci=None
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.dosis = dosis
        self.ci = ci

    def to_JSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "dosis": self.dosis,
            "ci": self.ci,            
        }
