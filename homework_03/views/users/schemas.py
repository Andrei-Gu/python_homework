from uuid import uuid4

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=15)


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int


def generate_token() -> str:
    return str(uuid4())


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)
