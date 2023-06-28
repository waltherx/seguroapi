from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User:
    def __init__(
        self,
        id=None,
        nameuser=None,
        password=None,
        email=None,
        estado=None,
        token=None,
        idrol=None,
        ci_persona=None,
    ) -> None:
        self.id = id
        self.nameuser = nameuser
        self.password = password
        self.email = email
        self.estado = estado
        self.token = token
        self.idrol = idrol
        self.ci_persona = ci_persona

    def to_JSON(self):
        return {
            "id": self.id,
            "nameuser": self.nameuser,
            "password": self.password,
            "email": self.email,
            "estado": self.estado,
            "token": self.token,
            "idrol": self.idrol,
            "ci_persona": self.ci_persona,
        }

    @classmethod
    def encrypt_password(self, pwd: str):
        return generate_password_hash(pwd)

    @classmethod
    def verificar_password(self, encriptado, password):
        return check_password_hash(encriptado, password)


class UserLogged(UserMixin):
    def __init__(
        self,
        id: int,
        nameuser: str,
        email: str,
        password: str,
        ci_persona: int,
        nombres: str,
        apellidos: str,
        foto_url: str,
        rol: int,
    ):
        self.id = id
        self.nameuser = nameuser
        self.email = email
        self.password = password
        self.ci_persona = ci_persona
        self.nombres = nombres
        self.apellidos = apellidos
        self.foto_url = foto_url
        self.rol = rol

    def __str__(self) -> str:
        return f"UserLogged: idu={self.id}, nameuser={self.nameuser}, email={self.email}, ci={self.ci_persona}, nombres={self.nombres}, apellidos={self.apellidos}, foto_url={self.foto_url}, rol={self.rol}"
