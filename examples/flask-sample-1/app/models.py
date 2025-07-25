import uuid

USERS_DB = []

class User:
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
