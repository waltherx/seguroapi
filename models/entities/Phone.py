class Phone:
    def __init__(self, id, numero=None) -> None:
        self.id = id
        self.numero = numero

    def to_JSON(self):
        return {
            "id": self.id,
            "numero": self.numero,
        }
