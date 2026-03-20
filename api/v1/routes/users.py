# Let's expose the users endpoint
from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from api.v1.services.users_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

# Pydantic Model to validate the user data
class UserCreate(BaseModel):
    name: str
    email: EmailStr  #uv add 'pydantic[email]'
    phone: str

class UserUpdate(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

# url: localhost:8000/api/v1/users/ -- GET
@router.get("/")
def get_users(user_service: UserService = Depends(UserService.get_user_service)):
    return user_service.get_users()

# url: localhost:8000/api/v1/users -- POST
@router.post("/")
def create_user(user: UserCreate, user_service: UserService = Depends(UserService.get_user_service)): 
    # the dict will allow any random data also to be sent, we can use pydantic models to validate the data
    print(f"Received user data: {user}")
    return user_service.create_user(user)

# url: localhost:8000/api/v1/users/1 or /2 -- GET
@router.get("/{user_id}")
def get_user_by_id(user_id: int, user_service: UserService = Depends(UserService.get_user_service)):
    print(f"Received user id: {user_id}")
    return user_service.get_user_by_id(user_id)

# url: localhost:8000/api/v1/users/1 or /2 -- PUT
@router.put("/{user_id}")
def update_user_by_id(user_id: int, user: UserUpdate, user_service: UserService = Depends(UserService.get_user_service)):
    print(f"Received and user data: {user} and user id: {user_id}")
    return user_service.update_user_by_id(user_id, user)

# url: localhost:8000/api/v1/users/1 or /2 -- DELETE
@router.delete("/{user_id}")
def delete_user_by_id(user_id: int, user_service: UserService = Depends(UserService.get_user_service)):
    print(f"Received user id: {user_id}")
    return user_service.delete_user_by_id(user_id)

