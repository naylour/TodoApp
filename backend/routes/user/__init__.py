from fastapi.routing import APIRouter
from .model import User, UserCreate, UserPatch, UserDTO
from database import connection
from ulid import ULID
from argon2 import PasswordHasher
from datetime import datetime

hasher = PasswordHasher()

router = APIRouter(
    prefix='/user'
)

@router.get('/')
async def user_find_all() -> list[UserDTO]:
    return True

@router.get('/{id}')
async def user_find() -> UserDTO:
    return True

@router.post('/')
async def user_create(data: UserCreate) -> UserDTO:
    cursor = connection.cursor()

    cursor.execute(f'''
        INSERT INTO User (id, last_name, first_name, username, password, updated_at)
        VALUES (?, ?, ?, ?, ?, ?) RETURNING changes();
    ''', (str(ULID()), data.last_name, data.first_name, data.username, hasher.hash(data.password), datetime.now()))

    res = cursor.execute('''
        SELECT id, last_name, first_name, username, updated_at FROM User WHERE username = '?';
    ''', (data.username))

    id, last_name, first_name, username, updated_at = res.fetchone()

    connection.commit()

    return UserDTO(
        id=id,
        last_name=last_name,
        first_name=first_name,
        username=username,
        updated_at=updated_at
    )

@router.patch('/{id}')
async def user_create(id: str, data: UserPatch) -> UserDTO:
    pass
