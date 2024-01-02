from pydantic import BaseModel, Field, EmailStr
import datetime


class User(BaseModel):
    username: str = Field(unique=True, mandatory=True)
    email: EmailStr = Field(examples=["ale@gmail.com"], mandatory=True)
    height: float = Field(mandatory=True)
    weight: float = Field(mandatory=True)
    birthdate: datetime.date = Field(mandatory=True)
