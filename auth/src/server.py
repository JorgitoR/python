from fastapi import FastAPI
from infra.http.register import get_register_router
from ecase.service import AuthManagerDepencency
from infra.db.sql import SQL
from infra.db.database import DatabaseConnection

db_conn = DatabaseConnection()
sql_db = SQL(db_conn)

app = FastAPI(title="Authentication API", version="1.0")

def get_auth_manager():
    return AuthManagerDepencency(sql_db)

app.include_router(get_register_router(get_auth_manager), prefix="/auth", tags=["Authentication"])