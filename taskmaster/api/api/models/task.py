from datetime import datetime

class Task:
    def __init__(self, title, dedscription, status):
        self.id = None # sera défini lors de l'ajout à la liste
        self.title = title
        self.dedscription = dedscription
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "dedscription": self.dedscription,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }