from typing import Type
from utils.schema import BU
from domain.ports.Idb import IDatabase
from urllib.parse import urlparse
import pymysql
from config import DB_TYPE, SQL_DATABASE_URL, AWS_REGION, DYNAMODB_TABLE_NAME

class SQL(IDatabase):

    def __init__(self):
        self.create_table()

    @property
    def create_connection(self):
        """ Inicia la conexión con la base de datos SQL """
        try:
            db_url = urlparse(SQL_DATABASE_URL)

            self.sqlconnection = pymysql.connect(
                host=db_url.hostname,
                user=db_url.username,
                password=db_url.password,
                database=db_url.path.lstrip("/"),  # Elimina la barra inicial `/`
                port=db_url.port or 3306  # Si no hay puerto, usa el default de MySQL
            )
            self.cursor = self.sqlconnection.cursor()
            print("Conexión establecida con la base de datos SQL")
        except pymysql.Error as e:
            print(f"Error al conectar con SQL: {e}")
            self.sqlconnection = None
            self.cursor = None

    def close_sql_connection(self):
        """ Cierra la conexión SQL si está activa """
        if self.create_connection:
            try:
                self.create_connection.commit()
                self.cursor.close()
                self.sqlconnection.close()
            except pymysql.Error as e:
                print(f"Error al cerrar la conexión SQL: {e}")
            finally:
                self.sqlconnection = None
                self.cursor = None

    
    def create_table(self):
        """ Crea la tabla USERS con el esquema del modelo BU """
        conn, cursor = self.create_connection
        query = """
        CREATE TABLE IF NOT EXISTS USERS (
            email VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255),
            is_active BOOLEAN DEFAULT TRUE,
            is_superuser BOOLEAN DEFAULT FALSE,
            is_verified BOOLEAN DEFAULT FALSE,
            phone BIGINT DEFAULT 0
        );
        """
        cursor.execute(query)
        conn.commit()
        self.close_sql_connection

    def save(self, data: Type[BU]):
        """ Guarda un usuario en la base de datos SQL """
        try:
            conn, cursor = self.create_connection
            query = """
            INSERT INTO USERS (email, password, name, is_active, is_superuser, is_verified, phone) 
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (
                data.email, data.password, data.name, data.is_active, data.is_superuser, data.is_verified, data.phone
            ))
            conn.commit()
            return {"message": "Usuario guardado en SQL", "user": data.model_dump()}
        except Exception as e:
            print(f'Error guardando usuario en SQL: {e}')
            return {"error": str(e)}
        finally:
            self.close_sql_connection
    
    def get(self, email: str):
        """ Obtiene un usuario por su email en SQL """
        try:
            _, cursor = self.create_connection
            query = "SELECT * FROM USERS WHERE email = %s;"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            if user:
                return {
                    "email": user[0],
                    "password": user[1],
                    "name": user[2],
                    "is_active": bool(user[3]),
                    "is_superuser": bool(user[4]),
                    "is_verified": bool(user[5]),
                    "phone": user[6]
                }
            return None
        except Exception as e:
            print(f'Error obteniendo usuario en SQL: {e}')
            return {"error": str(e)}
        finally:
            self.close_sql_connection
    
    def update(self, email: str, new_data: Type[BU]):
        """ Actualiza un usuario en SQL """
        try:
            conn, cursor = self.create_connection
            query = """
            UPDATE USERS 
            SET password = %s, name = %s, is_active = %s, is_superuser = %s, is_verified = %s, phone = %s
            WHERE email = %s;
            """
            cursor.execute(query, (
                new_data.password, new_data.name, new_data.is_active, new_data.is_superuser, new_data.is_verified, new_data.phone, email
            ))
            conn.commit()
            return {"message": "Usuario actualizado en SQL", "user": new_data.model_dump()}
        except Exception as e:
            print(f'Error actualizando usuario en SQL: {e}')
            return {"error": str(e)}
        finally:
            self.close_sql_connection


    