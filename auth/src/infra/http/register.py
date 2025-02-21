from ecase.service import AuthManagerDepencency
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    
def get_register_router(
        get_auth_manager: AuthManagerDepencency
) -> APIRouter:
    
    router = APIRouter()

    @router.post("/login", status_code=200, name="login")
    async def login(user: UserLogin, auth_service: AuthManagerDepencency = Depends(get_auth_manager)):
        try:
            response = auth_service.login(user.email, user.password)
            return response
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    @router.post("/register", status_code=201, name="register")
    async def register(user: UserRegister, auth_service: AuthManagerDepencency = Depends(get_auth_manager)):
        try:
            response = auth_service.sign_up(user.email, user.password)
            return response
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    return router

