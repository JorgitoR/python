from ecase.service import AuthManagerDepencency

from fastapi import FastAPI, APIRouter


def get_register_router(
        get_auth_manager: AuthManagerDepencency
) -> APIRouter:
    
    router = APIRouter()

    @router.post("/ragister", response_model="", status_code=200, name="register")
    async def register():
        get_auth_manager.login() 

    return router