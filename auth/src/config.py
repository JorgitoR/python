import os

DB_TYPE = os.getenv('DB_TYPE', 'nosql')

SQL_DATABASE_URL = os.getenv(
    'SQL_DATABASE_URL',
    'mysql+pymysql://admin:test123456As,@usersdb.cu904ok648go.us-east-1.rds.amazonaws.com/users_db'
)

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME", "auth")