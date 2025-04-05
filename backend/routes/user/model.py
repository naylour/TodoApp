from typing import Union

from pydantic import BaseModel
from ulid import ULID


class User(BaseModel):
    id: ULID

    last_name: Union[str, None]
    first_name: str

    username: str
    password: str

    updated_at: str

class UserDTO(BaseModel):
    id: ULID

    last_name: Union[str, None]
    first_name: str

    username: str

    updated_at: str


class UserCreate(BaseModel):
    last_name: Union[str, None]
    first_name: str

    username: str
    password: str

class UserPatch(BaseModel):
    last_name: Union[str, None]
    first_name: Union[str, None]

    username: Union[str, None]
    password: Union[str, None]
