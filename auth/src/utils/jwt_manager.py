import os 
from typing import Union, List, Optional
from pydantic import SecretStr
import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone



SecretType = Union[str, SecretStr]

JWT_ALGORITHM = "HS256"

load_dotenv()

def _get_secret_value(secret: SecretType):
    if isinstance(secret, SecretStr):
        return secret.get_secret_value()
    return secret


def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))


def generate_jwt(data: dict, secret: SecretStr, lifetime_seconds: Optional[int] = None, algorithm: str = JWT_ALGORITHM):

    payload = data.copy()
    if lifetime_seconds:
        expire = datetime.now(timezone.utc) +  timedelta(seconds=lifetime_seconds)
        payload["exp"] = expire
    return jwt.encode(payload, _get_secret_value(secret), algorithm=algorithm)

def decode_jwt(encode_jwt: str, secret: SecretStr, audience: List[str], algorightms: List[str] = [JWT_ALGORITHM]) -> dict:
    try:
        jwt_decode = jwt.decode(
            encode_jwt,
            _get_secret_value(secret),
            audience=audience,
            algorithms=algorightms
        )
    except:
        return {"token error:" "Token Has epired"} 
    else:
        return jwt_decode