class Phone:
    def __init__(self, id, numero=None,referencia=None, ci=None) -> None:
        self.id = id
        self.numero = numero
        self.referencia = referencia
        self.ci = ci

    def to_JSON(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "referencia": self.referencia,
            "ci": self.ci
        }
