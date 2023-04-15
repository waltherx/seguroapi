class Emergencia:
    def __init__(
        self,
        id=None,
        titulo=None,
        fecha_creacion=None,
        fecha_envio=None,
        user_destino=None,
        user_remitente=None,
        leido=None,
    ) -> None:
        self.id = id
        self.titulo = titulo
        self.fecha_creacion = fecha_creacion
        self.fecha_envio = fecha_envio
        self.user_destino = user_destino
        self.user_remitente = user_remitente
        self.leido = leido

    def to_JSON(self):
        return {
            "id": self.id,
            "titulo":self.titulo,
            "fecha_creacion": self.fecha_creacion,
            "fecha_envio": self.fecha_envio,
            "user_destino": self.user_destino,
            "user_remitente": self.user_remitente,
            "leido": self.leido,
        }
