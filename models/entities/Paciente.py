class Paciente:
    def __init__(
        self,
        id=None,
        tipoSangre=None,
        hipertencion=None,
        altura=None,
        peso=None,
        ci_persona=None,
    ) -> None:
        self.id = id
        self.tipoSangre = tipoSangre
        self.hipertencion = hipertencion
        self.altura = altura
        self.peso = peso
        self.ci_persona = ci_persona

    def to_JSON(self):
        return {
            "id": self.id,
            "tipoSangre": self.tipoSangre,
            "hipertencion": self.hipertencion,
            "altura": self.altura,
            "peso": self.peso,
            "ci_persona": self.ci_persona,
        }
