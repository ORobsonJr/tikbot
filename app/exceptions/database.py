
class UserAlreadyExists(Exception):
    """The user provided already exists in DB"""
    def __init__(self, user: str):
        self.message = f"The user {user} already exists in database, the attempt to handle duplicate user failed"
        super().__init__(self.message)
