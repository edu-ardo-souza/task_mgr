from datetime import datetime
import Status

class Task:
    def __init__(self, title: str, description: str, creationDate: datetime, status: Status) -> None:
        self.title = title
        self.description = description
        self.creationDate = creationDate
        self.status = status