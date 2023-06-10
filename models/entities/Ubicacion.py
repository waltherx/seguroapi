class Ubicacion:
    def __init__(
        self,
        id: int = None,
        latitud: float = None,
        longitud: float = None,
        hora: str = None,
        persona_ci: int = None,
        dispositivo_id: int = None,
    ) -> None:
        self.id = id
        self.latitud = latitud
        self.longitud = longitud
        self.hora = hora
        self.persona_ci = persona_ci
        self.dispositivo_id = dispositivo_id

    def __repr__(self) -> str:
        return (
            f"{self.dispositivo_id} : ({self.latitud}, {self.longitud}) ->{self.hora}"
        )

    def to_JSON(self) -> str:
        return {
            "id": self.id,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "hora": self.hora,
            "persona_ci": self.persona_ci,
            "dispositivo_id": self.dispositivo_id,
        }