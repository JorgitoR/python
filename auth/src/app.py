from ecase.service import ServiceAuth
from infra.db.sql import SQL

# Iniciar Conexion y servicios
sql_db = SQL()
auth = ServiceAuth(sql_db)


## Función para imprimir secciones organizadas en la terminal
def print_section(title):
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50 + "\n")

# Función para imprimir resultados de manera ordenada
def print_result(action, result):
    print(f"[{action}] ➜ {result}\n")

# Probar sign_up
'''
print_section("Testing User Registration")
print_result("Sign Up (test@example.com)", auth.sign_up("test@example.com", "secure123"))
print_result("Sign Up (test@example.com) - Duplicate", auth.sign_up("test@example.com", "12345678A"))
print_result("Sign Up (new@example.com) - Weak Password", auth.sign_up("new@example.com", "123"))
'''
# Probar si se trae toda la información del usuario
print_section("Fetching User Information")
print_result("Get User (user1@example.com)", sql_db.get('bermeo22@hotmail.com'))

# Probar login
'''
print_section("Testing User Login")
print_result("Login (Correct Password)", auth.login("test@example.com", "secure123"))
print_result("Login (Incorrect Password)", auth.login("test@example.com", "wrongpass"))
print_result("Login (Non-existent User)", auth.login("notfound@example.com", "password"))
'''