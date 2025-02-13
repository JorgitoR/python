from domain.Iauth import Iauth
from domain.ports.Idb import IDatabase
from utils.exceptions import UserAlreadyExist


class ServiceAuth(Iauth):

    def __init__(self, db: IDatabase):
        self.database = db

    def login(self, email:str, password:str):
        user = self.database.get(email)
        if user is not None:
            if password == user[1]: 
                return {"status_code": 200, "message": "User has been logged succesfully"}
            else:
                return {"status_code": 403, "message": "Invalid password"}
        else:
            return {"status_code": 404, "message": "User not found"}


    def sign_up(self, email:str, password:str):
        # TODO: Validar que el usuario no exista en db
        try:
            user = self.database.get(email)
            if user is not None:
                raise UserAlreadyExist(status_code=409, msg="Usuario ya exite")

            # TODO: Validar tamaño de contraseña
            if len(password) <= 5:
                return {"status_code": 400, "message": "Password should be greater than 5 characters"}

            payload = {
                "email": email,
                "password": password
            }
            
            save_user = self.database.save(payload)
            if save_user:
                return {"status_code": 201, "message": "User has been created succesfully"}

        except Exception as e:
            raise e

        else:
            return {"status_code": 400, "message": "failed to save the user"}
    
        finally:
            pass 



AuthManagerDepencency = ServiceAuth