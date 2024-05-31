from pydantic import BaseModel, Field
import uuid

# ToBeDone: creationDate as datetime, status as model.Status
class Task(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    creationDate: str = Field(...)
    status: str = Field(...)