class Phone:
    def __init__(self, id, numero=None,referencia=None, ci_persona=None) -> None:
        self.id = id
        self.numero = numero
        self.referencia = referencia
        self.ci_persona = ci_persona

    def to_JSON(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "referencia": self.referencia,
            "ci_persona": self.ci_persona
        }
