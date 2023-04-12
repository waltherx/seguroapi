from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
	def __init__(
		self, id=None, nameuser=None, password=None, email=None, estado=None,token=None, idrol=None
	) -> None:
		self.id = id
		self.nameuser = nameuser
		self.password = password
		self.email = email
		self.estado = estado
		self.token = token
		self.idrol = idrol

	def to_JSON(self):
		return {
			"id": self.id,
			"nameuser": self.nameuser,
			"password": self.password,
			"email": self.email,
			"estado": self.estado,
   			"token": self.token,
			"idrol": self.idrol,
		}
  
	@classmethod
	def verificar_password(self, encriptado, password):
		return check_password_hash(encriptado, password)
  
