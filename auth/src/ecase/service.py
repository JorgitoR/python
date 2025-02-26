from domain.Iauth import Iauth
from domain.ports.Idb import IDatabase
from utils.exceptions import UserAlreadyExist, UserNotFound, InvalidPassword, WeakPassword, FailedToSaveUser
from typing import Type
from utils.schema import BaseUserCreate

class ServiceAuth(Iauth):

    def __init__(self, db: IDatabase):
        self.database = db

    def login(self, email:str, password:str):
        user = self.database.get(email)
        if user is not None:
            if password == user[1]: 
                return {"status_code": 200, "message": "User has been logged succesfully"}
            else:
                raise InvalidPassword(status_code=403, msg="Invalid password")
        else:
            raise UserNotFound(status_code=404, msg="User not found")


    def sign_up(self, data: BaseUserCreate):
        # TODO: Validar que el usuario no exista en db
        try:
            user = self.database.get(data.email)
            if user is not None:
                raise UserAlreadyExist(status_code=409, msg="User already exist")

            # TODO: Validar tamaño de contraseña
            if len(data.password) <= 5:
                raise WeakPassword(status_code=400, msg="Password should be greater than 5 characters")

            save_user = self.database.save(data)

        except Exception as e:
            raise e

        else:
            return save_user
    
        finally:
            pass 



AuthManagerDepencency = ServiceAuth