from fastapi import FastAPI
from utils import schema
from infra.http.register import get_register_router
from ecase.service import AuthManagerDepencency
from infra.db.sql import SQL
from infra.db.nosql import NoSQL
from infra.db.database import DatabaseConnection

db_conn = DatabaseConnection()
sql_db = SQL(db_conn)

nosql_db = NoSQL()

app = FastAPI(title="Authentication API", version="1.0")

def get_auth_manager():
    yield AuthManagerDepencency(nosql_db)

class UserCreate(schema.BaseUserCreate):
    pass 

app.include_router(get_register_router(get_auth_manager, UserCreate), prefix="/auth", tags=["Authentication"])