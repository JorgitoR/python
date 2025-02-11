from domain.Iauth import Iauth
from domain.ports.Idb import IDatabase

class ServiceAuth(Iauth):

    def __init__(self, db: IDatabase):
        self.database = db

    def login(self, email:str, password:str):
        
        # TODO: Validar que el usuario no exista en db
        user = self.database.get(email)
        if user is not None:
            return {"status_code": 404, "message": "User already exist"}

        # TODO: Validar tamaño de contraseña
        if len(password) <= 5:
            return {"status_code": 404, "message": "Password should be greater than 5 characters"}

        payload = {
            "email": email,
            "password": password
        }
        
        save_user = self.database.save(payload)
        if save_user:
            return {"status_code": 200, "message": "ok"}
        
        return {"status_code": 400, "message": "failed to save the user"}

    def sign_up(self):
        pass



    