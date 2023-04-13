class Token:
    def __init__(
        self, id=None, user_id=None, token=None, create_at=None, update_at=None
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.token = token
        self.create_at = create_at
        self.update_at = update_at

    def to_JSON(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "token": self.token,
            "create_at": self.create_at,
            "update_at": self.update_at,
        }
