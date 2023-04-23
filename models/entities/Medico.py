class Medico:
	def __init__(self,id=None, especialidad=None, hospital_id=None, ci_persona=None) -> None:
		self.id = id
		self.especialidad = especialidad
		self.hospital_id = hospital_id
		self.ci_persona = ci_persona

	def to_JSON(self):
		return {
			"id": self.id,
			"especialidad": self.especialidad,
			"hospital_id": self.hospital_id,
			"ci_persona": self.ci_persona,
		}
