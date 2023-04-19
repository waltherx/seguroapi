class Medico:
	def __init__(self,id=None, especialidad=None, hospital_id=None, user_id=None) -> None:
		self.id = id
		self.especialidad = especialidad
		self.hospital_id = hospital_id
		self.user_id = user_id

	def to_JSON(self):
		return {
			"id": self.id,
			"especialidad": self.especialidad,
			"hospital_id": self.hospital_id,
			"user_id": self.user_id,
		}
