from werkzeug.security import generate_password_hash, check_password_hash


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
	"""
	@property
	def password(self):
		raise AttributeError("password is not a readable attribute")

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
	"""
	# Flask-Login integration
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def is_admin(self):
		return self.admin
