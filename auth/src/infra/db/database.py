import os 
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DB_DIR = os.path.join(BASE_DIR, "../../data")  
os.makedirs(DB_DIR, exist_ok=True)  

DATABASE_NAME = os.path.join(DB_DIR, "users.db")  


class DatabaseConnection():
    def __init__(self):
        self.sqlconnection = None
        self.cursor = None
    
    def get_connection(self):
        if self.sqlconnection is None:
            try:
                self.sqlconnection = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
                self.cursor = self.sqlconnection.cursor()
            except sqlite3.Error as e:
                print(f'Error attemping to establish connection with the database: {e}')
                return None, None
        if self.cursor is None:
            self.cursor = self.sqlconnection.cursor()
        return self.sqlconnection, self.cursor

    def close_connection(self):
        if self.sqlconnection is not None:
            try:
                if self.sqlconnection.in_transaction:
                    self.sqlconnection.commit()
                if self.cursor is not None:
                    self.cursor.close()
                self.sqlconnection.close()
            except sqlite3.Error as e:
                print(f'Error while closing the database connection: {e}')
            else:
                pass
            finally:
                self.cursor = None
                self.sqlconnection = None

    
    def create_table(self):
        conn, cursor = self.get_connection()
        if conn is not None and cursor is not None:
            try:
                table = """ CREATE TABLE IF NOT EXISTS USERS(
                            email VARCHAR(255) NOT NULL,
                            password VARCHAR(255) NOT NULL
                        );"""
                cursor.execute(table)
                conn.commit()
            except sqlite3.Error as e:
                print(f'Error while creating the table: {e}')
            finally:
                self.close_connection()


        
