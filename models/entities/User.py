class User:
    def __init__(
        self, id=None, nameuser=None, password=None, email=None, estado=None, idrol=None
    ) -> None:
        self.id = id
        self.nameuser = nameuser
        self.password = password
        self.email = email
        self.estado = estado
        self.idrol = idrol

    def to_JSON(self):
        return {
            "id": self.id,
            "nameuser": self.nameuser,
            "password": self.password,
            "email": self.email,
            "estado": self.estado,
            "idrol": self.idrol,
        }
