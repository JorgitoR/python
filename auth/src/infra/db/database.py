import os
import pymysql
import boto3
from urllib.parse import urlparse
from config import DB_TYPE, SQL_DATABASE_URL, AWS_REGION, DYNAMODB_TABLE_NAME


class DatabaseConnection:
    def __init__(self):
        self.sqlconnection = None
        self.cursor = None

        if DB_TYPE == "sql":
            self.connect_sql()

        elif DB_TYPE == "nosql":
            self.db_type = "nosql"
            self.dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
            self.table = self.dynamodb.Table(DYNAMODB_TABLE_NAME)
        else:
            raise ValueError("DB_TYPE debe ser 'sql' o 'nosql'")

    def connect_sql(self):
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

    def get_sql_connection(self):
        """ Devuelve la conexión SQL si DB_TYPE es 'sql' """
        if self.sqlconnection is None or self.cursor is None:
            self.connect_sql()  # 🔹 Reconectar si es necesario
        return self.sqlconnection, self.cursor
    
    def get_nosql_connection(self):
        """ Devuelve la conexión NoSQL si DB_TYPE es 'nosql' """
        if self.db_type == "nosql":
            return self.table
        return None

    def close_sql_connection(self):
        """ Cierra la conexión SQL si está activa """
        if self.sqlconnection:
            try:
                self.sqlconnection.commit()
                self.cursor.close()
                self.sqlconnection.close()
            except pymysql.Error as e:
                print(f"Error al cerrar la conexión SQL: {e}")
            finally:
                self.sqlconnection = None
                self.cursor = None


        
