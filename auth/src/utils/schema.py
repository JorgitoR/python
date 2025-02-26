from typing import TypeVar, Optional
from pydantic import EmailStr, BaseModel


class BaseUserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    phone: Optional[int] = 0
 

BU = TypeVar("BU", bound=BaseUserCreate)
