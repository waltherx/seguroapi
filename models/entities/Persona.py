class Persona:
    def __init__(
        self,
        ci=None,
        nombres=None,
        apellidos=None,
        fechaNac=None,
        licVehicular=None,
        foto=None,
        tipoSangre=None,
        hipertencion=None,
        altura=None,
        peso=None,
        direccion=None,
    ) -> None:
        self.ci = ci
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaNac = fechaNac
        self.licVehicular = licVehicular        
        self.foto = foto
        self.tipoSangre = tipoSangre
        self.hipertencion = hipertencion
        self.altura = altura
        self.peso = peso
        self.direccion = direccion

    def to_JSON(self):
        return {
            "ci": self.ci,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "fechaNac": self.fechaNac,
            "licVehicular" : self.licVehicular,
            "foto": self.foto,
            "tipoSangre": self.tipoSangre,
            "hipertencion": self.hipertencion,
            "altura": self.altura,
            "peso": self.peso,
            "direccion": self.direccion,
        }
