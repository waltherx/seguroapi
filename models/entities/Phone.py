class Phone:
    def __init__(self, id, numero=None, ci=None) -> None:
        self.id = id
        self.numero = numero
        self.ci = ci

    def to_JSON(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "ci": self.ci
        }
