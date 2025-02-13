from domain.ports.Idb import IDatabase
from .database import DatabaseConnection

class SQL(IDatabase):

    def __init__(self, db: DatabaseConnection):
        self.db = db

    def save(self, data:dict):
        # TODO: persist logic with real database
        try:
            conn, cursor = self.db.get_connection()
            cursor.execute("INSERT INTO USERS (email, password) VALUES (?, ?) ", (data['email'], data['password']))
            conn.commit()
            return True
        except Exception as e:
            print(f'Error while saving user information: {e}')
            return False
        finally:
            self.db.close_connection()

    def get(self, email:str):
        try:
            _, cursor = self.db.get_connection()
            cursor.execute("SELECT * FROM USERS WHERE email = ?", (email,))
            user = cursor.fetchone()
            if user:
                return (user[0], user[1])
            return None
        except Exception as e:
            print(f'Error getting the email information: {e}')
            return None 
        finally:
            self.db.close_connection()

    def update(self, data, new_password):
        try:
            conn, cursor = self.db.get_connection()
            cursor.execute("UPDATE USERS SET password  = ? WHERE email = ?", (new_password, data['email']))
            conn.commit()
            print("Password updated successfully.")
            return True
        except Exception as e:
            print(f'Error while updating user information: {e}')
            return False
        finally:
            self.db.close_connection()


    