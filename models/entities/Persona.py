class Persona:
    def __init__(
        self,
        ci=None,
        nombres=None,
        apellidos=None,
        fecha_nacimiento=None,
        foto_url=None,
        foto_name=None,
        direccion=None,
        genero=None,
        estado_civil=None,
    ) -> None:
        self.ci = ci
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.foto_url = foto_url
        self.foto_name = foto_name
        self.direccion = direccion
        self.genero = genero
        self.estado_civil = estado_civil

    def to_JSON(self):
        return {
            "ci": self.ci,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "fechaNac": self.fechaNac,
            "foto_url" : self.foto_url,
            "foto_name": self.foto_name,            
            "direccion": self.direccion,
            "genero": self.genero,
            "estado_civil": self.estado_civil,
        }
