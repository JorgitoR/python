
from sqlalchemy import create_engine, text

# 🔹 Reemplaza con los datos correctos de tu RDS
DATABASE_URL = "mysql+pymysql://admin:test123456As,@usersdb.cu904ok648go.us-east-1.rds.amazonaws.com/users_db"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    # 🔹 Obtener todas las tablas
    result = connection.execute(text("SHOW TABLES;"))
    tables = [row[0] for row in result]  # 🔥 Lista con los nombres de las tablas

    print("\n📌 Tablas en la base de datos:")
    for table in tables:
        print(f"✅ {table}")

    # 🔹 Obtener datos de cada tabla
    for table in tables:
        print(f"\n📌 Contenido de la tabla: {table}")
        try:
            data = connection.execute(text(f"SELECT * FROM {table};"))
            rows = data.fetchall()

            if not rows:
                print("⚠️ La tabla está vacía.")
            else:
                for row in rows:
                    print(row)  # 🔥 Imprime cada fila de la tabla

        except Exception as e:
            print(f"❌ Error al consultar la tabla {table}: {e}")

