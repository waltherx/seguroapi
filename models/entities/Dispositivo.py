class Dispositivo:
    def __init__(
        self,
        id: int = None,
        nombre: str = None,
    ) -> None:
        self.id = id
        self.nombre = nombre

    def __repr__(self) -> str:
        return f"{self.id} - {self.nombre}"

    def to_JSON(self) -> str:
        return {
            "id": self.id,
            "nombre": self.nombre,
        }
