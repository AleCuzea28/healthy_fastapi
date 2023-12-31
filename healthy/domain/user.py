from pydantic import BaseModel, Field
import datetime


class User(BaseModel):
    username: str = Field(unique=True, mandatory=True)
    email: str = Field(unique=True, mandatory=True)
    height: float = Field(mandatory=True)
    weight: float = Field(mandatory=True)
    birthdate: datetime.date = Field(mandatory=True)
